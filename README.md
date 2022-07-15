# Monte Carlo Simulation
Anne Louise Seekford  
DS5100 Final Project


## Metadata  

Author: Anne Louise Seekford  
Package: 
```montecarlo_simulator```

## Synopsis  

**Installation**  

To install the ```montecarlo_simulator``` package, begin by cloning this GitHub Repository. You can do this in your local machine's terminal by typing:
```
$ git clone https://github.com/alseekford/MonteCarloSimulation_DS5100.git
``` 
Next, go into the file directory by:
```
$ cd MonteCarloSimulation_DS51000
```   
<br/>

To actually install the package, then run the command ```$ !pip install -e .``` .  
If installation was successful, you should see something like: 
```m
Obtaining file:///Users/alseekford/5100/final/MonteCarloSimulation_DS5100
Installing collected packages: MonteCarlo-DS5100
  Running setup.py develop for MonteCarlo-DS5100
Successfully installed MonteCarlo-DS5100
```
<br/>

**Importing**

To import the three classes (Die, Game, and Analyzer) within the montecarlo.py file from the package, simply run: 

```python
$ python3

>>> from montecarlo_simulator.montecarlo import Die, Game, Analyzer 
```
<br/>

**Creating Dice**

Die have two properties: *Faces* and *Weights*. All die are initialized with *all* weights set as $1.0$. 
To create a die, we first supply the face values.  

For the sake of example, let's say we're rolling a Magic 8-Ball.
```python
>>> magic_ball = Die(['Yes', 'Maybe', 'Never', "I'm Not Sure - Roll Again", 'Without a Doubt'])
```

As we all know, Magic 8-Ball's tend to show us what we want to hear - i.e. have a slight bias towards the more affirmative responses.  

To mimic this bias, let's change the weights of the positive responses:

```python
>>> magic_ball.change_weight('Yes', 2)
>>> magic_ball.change_weight('Without a Doubt', 3)
```

To check and ensure the weights were properly changed, we can run:
```python
>>> magic_ball.show_die()
```
Which will return our current die:

<p align="center">
  <img width="188" alt="Screen Shot 2022-07-15 at 3 25 07 PM" src="https://user-images.githubusercontent.com/71660299/179297082-c5feda06-c270-4be7-a56d-713d76942c88.png">
</p>



Now, we can roll our die! Let's just roll one time.
```python
>>> magic_ball.roll_die(1)
```

<br/>

**Playing Games**

To continue on with the Magic 8-Ball example, let's say you and three friends all want to ask the magic ball questions simultaneously.
To do that, we can pass four magic balls to our game!
```python
>>> magic_game = Die([magic_ball, magic_ball, magic_ball, magic_ball])
```
Note: all die passed do NOT need to be the same, but similar (i.e. same number of faces)

To roll each ball 3 times:
```python 
>>> magic_game.play(3)
```

To see the DataFrame of results for each of you and your friends magic balls:
```python 
>>> magic_game.show_results()
```

<br/>

**Analyzing Games**

Let's analyze our results! To do so, first we initialize.

```python
>>> magic_analyzer = Analyzer(magic_game)
```

From there, we can calculate the number of *Jackpots*, *Combinations*, and see the *value counts* of each Face rolled.

```python
jackpots = magic_analyzer.jackpot()
combinations = magic_analyzer.combo()
answer_counts = magic_analyzer.faces_per_roll()
```

<br/>

## API Description  

Contains descriptions of all three classes (Die, Game, and Analzyer) and their corresponding methods and attributes.

#### class Die

**class Die** 

#### class Game

g

#### class Analyzer

a


<br/>

## Manifest  
File directory of repo:
```
montecarlo_simulator
    __init__.py
    montecarlo.py

.gitignore
LICENSE
README.md
final-project-submission.ipynb
mc_scenarios.ipynb
montecarlo_test.py
montecarlo_test.txt
setup.py
```
