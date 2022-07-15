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

```
$ python3

>>> from montecarlo_simulator.montecarlo import Die, Game, Analyzer 
```
<br/>

**Creating Dice**

Die have two properties: *Faces* and *Weights*. All die are initialized with *all* weights set as $1.0$. 
To create a die, we first supply the face values.  

For the sake of example, let's say we're rolling a Magic 8-Ball.
```
>>> magic_ball = Die(['Yes', 'Maybe', 'Never', 'I'm Not Sure - Roll Again', 'Without a Doubt'])
```

As we all know, Magic 8-Ball's tend to show us what we want to hear - i.e. have a slight bias towards the more affirmative responses.  

To mimic this bias, let's change the weights of the positive responses:

```
>>> magic_ball.change_weight('Yes', 2)
>>> magic_ball.change_weight('Without a Doubt', 3)
```


<br/>

**Playing Games**


<br/>

**Analyzing Games**


<br/>

## API Description  


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
