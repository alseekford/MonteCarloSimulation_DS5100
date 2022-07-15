import pandas as pd
import numpy as np

class Die: 
    """
    PURPOSE: Creates a die with n Faces and w Weights. Can be rolled to select a face

    METHODS: 
    __init__
    change_weight
    roll_die
    show_die
    """
    def __init__(self, faces):
        """
        PURPOSE: Initializes the Die class

        INPUTS: 
        faces      arr

        OUTPUTS: No outputs
        """
        self.faces = faces
        self.weights = []
        for i in range(len(self.faces)):
            self.weights.append(1.0)
        self._dice = pd.DataFrame(data = {'Faces':self.faces, 'Weights':self.weights})
    
    def change_weight(self, face_value, new_weight):
        """
        PURPOSE: Changes the weight value of a designated face.
        
        INPUTS:
        face_value   str
        new_weight   float

        OUTPUTS: Raises an Exception if the new weight is not a float or int value.
        """
        # Check to see if the face is valid
        if face_value in self._dice['Faces'].values:
            # Check to see if the weight is valid - and change if applicable
            if isinstance(new_weight, int):
                new_weight = float(new_weight)
                # Replace 
                self._dice.loc[self._dice.Faces == face_value, 'Weights'] = new_weight
            elif isinstance(new_weight, float):
                new_weight = new_weight
                self._dice.loc[self._dice.Faces == face_value, 'Weights'] = new_weight
            else:
                raise Exception('Please try again. New weight must be a float value.')
        else:
            print('Sorry, this face value does not exist. Try again.')

    
    def roll_die(self, n_rolls=1):
        """
        PURPOSE: Rolls the die n times and returns the result.
            
        INPUTS: 
        n_rolls     int; default=1

        OUTPUTS: Returns a list of the results.
        """
        results = []
        for i in range(n_rolls):
            result = self._dice.Faces.sample(weights=self._dice.Weights).values[0]
            results.append(result)
        return results
    
    def show_die(self):
        """
        PURPOSE: Prints the current die and corresponding weights.

        INPUTS: No inputs

        OUTPUTS: Returns the current die as a DataFrame
        """
        return pd.DataFrame(self._dice)
    
    
    
    
class Game(): 
    """
    PURPOSE: A game consists of rolling one or more dice of the same kind one or more times.

    METHODS: 
    __init__
    play
    show_results
    """
    def __init__(self, my_dice):
        """
        PURPOSE: Initializes a list of already-instantiated Die objects.

        INPUTS: 
        my_dice     arr

        OUTPUTS: No outputs
        """
        # self._dice takes an array
        self.dice = my_dice
        
        # Instantiate the DataFrame of the results for all die
        self._results = pd.DataFrame()



    
    def play(self, n_rolls):
        """
        PURPOSE: Rolls each die n_rolls number of times and returns the result of the most recent play.
        
        INPUTS:
        n_rolls   int

        OUTPUTS: No outputs
        """
    
        self.rolls = n_rolls

        roll_die = Game.roll_die

        for current_die in self.dice:
            row_result = current_die.roll_die(n_rolls)
            self._results[self.dice.index(current_die)] = row_result
            self._results.index.name = 'Roll_Number'
            self._results = self._results.rename_axis('Dice', axis='columns')
        
    
    def show_results(self, n_or_w= 'wide'):
        """
        PURPOSE: Shows you, as the user, the results of the most recent play. 
        
        INPUTS:
        n_or_w     str; must be either 'narrow' or 'wide'
        
        OUTPUTS: A dataframe with results - in either wide or narrow form.
        """
        # Regardless of narrow or wide, the index will be Roll Number
        self._results.index.name = 'Roll_Number'
        
        if n_or_w == 'wide':
            # 1 index: roll number
            # Columns: each die number
            return self._results
            
        elif n_or_w == 'narrow':
            # 2 column index: die #, roll number
            # Column: face rolled
            # narrow_dice = self._results.reset_index().set_index(['Dice','Roll_Number'])
            narrow_dice = self._results.T.stack().to_frame()
            return narrow_dice
        
        else: 
            # Raise an exception if the option is invalid
            raise ValueError('Invalid. You must denote either "narrow" or "wide". Please try again.')
            
            
class Analyzer(): 
    """
    PURPOSE: Takes the results of a single game and computes various descriptive statistical properties about it. 
    
    METHODS: 
    __init__
    faces_per_roll
    jackpot
    combo
    """
    def __init__(self, my_game):
        """
        PURPOSE: Initializes the Game.show_results and Die.show_die

        INPUTS: A game object

        OUTPUTS: No outputs
        """
        self.my_game = my_game
        
        # Infer datatype
        #self.data_type = type(self.my_game.iloc[:,0][0]) is str
        
        self.game_result = self.my_game.show_results() #Raf code
        
        
    
    def faces_per_roll(self):
        """
        PURPOSE: The number of times a given face appeared in each roll. 
                 Ex. if a roll of five dice has all sixes, then the counts 
                 for this roll would be 6 for the face value '6' and 0 for the other faces
        
        INPUTS: No inputs

        OUTPUTS: Returns a Series of the Face values
        """
        face_vals = self.my_game.show_results().apply(pd.Series.value_counts, axis=1).fillna(0).astype(int)
        return face_vals
        
    
    def jackpot(self):
        """
        PURPOSE: How many times a roll resulted in all faces being the same
                 Ex. all one for a six-sided die.

        INPUTS: No inputs

        OUTPUTS: Returns the number of Jackpots.
        """
        self.num_jackpots = 0 #Initialize as 0
        
        # Jackpot DataFrame ; Roll_Number as index, filled with Boolean values, then convert
        self.bool_df = self.game_result.eq(self.game_result.iloc[:,0], axis=0).all(1)
        self.jackpot_df = self.bool_df[self.bool_df]
        
        # Return the number of jackpots - AKA how many rows
        return len(self.jackpot_df)
        
    def combo(self):
        """
        PURPOSE: How many combination types of faces were rolled and their counts

        INPUTS: No inputs.

        OUTPUTS: Returns a DataFrame of Combos
        """
        self.combos = self.game_result.apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('n') #Raf code
        return self.combos           
        