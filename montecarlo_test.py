"""
AUTHOR: Anne Louise Seekford
CONTACT: bng3be@virginia.edu
"""


import pandas as pd
import numpy as np
import unittest

# Import montecarlo.py classes
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer


class MonteCarloTestSuite(unittest.TestCase):
    """
    TESTS FOR DIE CLASS (5)
    """
    
    def test_1__init__(self):
        """
        PURPOSE: to ensure initialization of all weights as 1
        
        INPUTS: no inputs
        
        OUTPUTS: passes test
        """
        die1 = Die(['clubs', 'hearts', 'spades', 'diamonds'])
        self.assertTrue(die1._dice.iloc[0,0] == 1)
    

    def test_2_change_weight_successfully(self):
        """
        PURPOSE: test change_weight method with a valid weight value (i.e. an integer) by weight of 'spades' changed to 4
        
        INPUTS: no inputs
        
        OUTPUTS: passes test
        """
        die2 = Die(['clubs', 'hearts', 'spades', 'diamonds'])
        die2.change_weight('spades', 4)
        new_weights = [1, 1, 4, 1]
        
        # Check
        self.assertEqual(die2.Weights, new_weights)
    
    
    def test_3_change_weight_to_fail(self):
        """
        PURPOSE: test change_weight method with a valid weight value (i.e. a string) by weight of 'clubs' changed to 'putter'
        
        INPUTS: no inputs
        
        OUTPUTS: passes test that raises an exception "Please try again. New weight must be a float value." indicating an invalid argument.
        """
        with self.assertRaises(Exception):
            die3 = Die(['clubs', 'hearts', 'spades', 'diamonds'])
            die3.change_weight('clubs', 'driver')
    
    
    def test_4_roll_die(self):
        """
        PURPOSE: returns the length of results that match the n_rolls argument
        
        INPUTS: no inputs
        
        OUTPUTS: passes test
        """
        die4 = Die(['maybe', 'yes', '100% no', 'try again'])
        rolly = die4.roll_die(n_rolls=4)
        
        # Check
        self.assertEqual(len(rolly), 4)
    
    
    def test_5_show_die(self):
        """
        PURPOSE: validates the DataFrame returned by show_die is correct
        
        INPUTS: no inputs
        
        OUTPUTS: passes test
        """
        die5 = Die(['one', 'one twice', 'one again'])
        expected = pd.DataFrame({'Faces':['one', 'one twice', 'one again'], 'Weights':[1, 1, 1]})
        
        # Check
        self.assertEqual(die5.show_die(), expected)
    
    
    """
    TESTS FOR GAME CLASS (5)
    """
    
    def test_6__init__(self):
        """
        PURPOSE: to ensure initialization
        
        INPUTS: no inputs
        
        OUTPUTS: passes test
        """
        die6 = [Die(['1', '2', '3']), Die(['4', '5', '6'])]
        my_game = Game(die6)
        
        # Check
        self.assertTrue(isinstance(my_game, Game))
    
    
    def test_7_play(self):
        """
        PURPOSE: checks the shape of results that match the n_rolls argument for each Die provided
        
        INPUTS: no inputs
        
        OUTPUTS: passes test
        """
        die7 = [Die(['a', 'b', 'c']), Die(['d', 'e', 'f'])]
        my_game = Game(die7)
        my_game.play(7)
        die7_results = my_game.show_results()
        expected = (7, 2)
        
        # Check
        self.assertEqual(die7_results.shape, expected)
    

    def test_8_wide_results(self):
        """
        PURPOSE: ensure the DataFrame will return 'wide' by default by matching the shape
        
        INPUTS: no inputs
        
        OUTPUTS: passes test
        """        
        die8 = [Die(['a', 'b', 'c']), Die(['d', 'e', 'f']), Die(['g', 'h', 'i'])]
        my_game = Game(die8)
        my_game.play(8)
        die8_results = my_game.show_results()
        expected = (8, 3)
        
        # Check
        self.assertEqual(die8_results.shape, expected)
        
    
    def test_9_narrow_results(self):
        """
        PURPOSE: ensure the DataFrame will return 'narrow' when passing the parameter, by matching the shape
        
        INPUTS: no inputs
        
        OUTPUTS: passes test
        """        
        die9 = [Die(['do', 're', 'mi']), Die(['fa', 'so', 'la'])]
        my_game = Game(die9)
        my_game.play(9)
        die9_results = my_game.show_results()
        expected = (18, 1)
        
        # Check
        self.assertEqual(die9_results.shape, expected)
    
    
    def test_10_fail_results(self):
        """
        PURPOSE: to ensure an exception is raised when a value other than 'narrow' or 'wide' is passed.
        
        INPUTS: no inputs
        
        OUTPUTS: passes test
        """        
        with self.assertRaises(Exception):
            die10 = [Die(['do', 're', 'mi']), Die(['fa', 'so', 'la'])]
            my_game = Game(die10)
            my_game.play(10)
            my_game.show_results(n_or_w = 'skinny queen')
    
    """
    TESTS FOR ANALYZER CLASS (4)
    """
    
    def test_11__init__(self):
        """
        PURPOSE: to ensure initialization
        
        INPUTS: no inputs
        
        OUTPUTS: passes test
        """        
        die11 = [Die(['am', 'i', 'init']), Die(['am', 'i', 'init'])]
        my_game = Game(die11)
        my_game.play(11)
        my_ana = Analyzer(my_game)
        
        # Check
        self.assertTrue(isinstance(my_ana.my_game), Game)
    

    def test_12_faces_per_roll(self):
        """
        PURPOSE: to ensure the number of columns matches the number of faces on the Die
        
        INPUTS: no inputs
        
        OUTPUTS: passes test
        """        
        die12 = [Die(['do', 're', 'mi']), Die(['fa', 'so', 'la'])]
        my_game = Game(die12)
        my_game.play(12)
        my_ana = Analyzer(my_game)
        counts = my_ana.faces_per_roll()
        expected = (12, 3)
        
        # Check
        self.assertEqual(counts.shape, expected)
    

    def test_13_jackpot(self):
        """
        PURPOSE: returns the proper number of times a roll resulted in all faces being the same as an INTEGER
        
        INPUTS: no inputs
        
        OUTPUTS: passes test
        """        
        die13 = [Die(['king', 'jack', 'ace']), Die(['two', 'joker', 'ace']), Die(['king', 'queen', 'two']), Die(['queen', 'ace', 'two'])]
        my_game = Game(die13)
        my_game.play(13)
        my_ana = Analyzer(my_game)
        jack = my_ana.jackpot()
        
        # Check
        self.assertTrue(type(jack) == int)
    

    def test_14_combo(self):
        """
        PURPOSE: the combos should be multi-indexed, so we can check by ensuring there is only one column. 
        
        INPUTS: no inputs
        
        OUTPUTS: passes test
        """        
        die14 = [Die(['ace', 'jack', 'one']), Die(['two', 'joker', 'ace'])]
        my_game = Game(die14)
        my_game.play(14)
        my_ana = Analyzer(my_game)
        comboo = my_ana.combo()
        
        # Check
        self.assertTrue(len(comboo.columns) == 1)
        
        
unittest.main(argv=['first-arg-is-ignored'], exit=False);           

# if __name__ == '__main__':
#     unittest.main(verbosity=3)        
    
