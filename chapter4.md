# Chapter 4: Capstone project

Welcome to chapter 4! If you made it here, congratulations! That means you already know a lot about programming in Python with PyGame (yay!). In this final chapter, you will implement your own version of the Whack-a-Mole game. There will be a solution provided, but keep in mind that there are multiple ways of implementing this game in PyGame – do it whichever way you think is best!

## Rules
The rules of Whack-A-Mole are as follows:
 
 * The board has 16 holes
 * When the game starts, a random number of moles should pop up
 * Every time the player hits a mole, the mole that was hit should disappear and
 * New moles should pop up from the surrounding holes which are empty
 * If there are already moles in any of the surrounding holes, they should disappear
 * The player wins if there are no moles left on the board

## Solution

We've attached a solution written in pseudoce below. The game logic is split into 3 parts: we have our Mole object, which represents each mole on the board, the `check_win()` function which checks if all the moles are gone from the board and lastly, we have the actual main loop which reads user input and carries out the appropiate action based on that – if the clicked hole has a mole in it, we remove it and flip the state of all surrounding holes (if there's a mole, remove it; if there's no mole, add one).

```pseudo
class Mole:
  initialise(x, y):
    image = load 'mole.jpg' image
    rect = get image's rectangle
    set rect's x and y coordinates to x and y
    visible = False
    
  show(visibility):
    visible = visibiltiy

check_win():
  if all moles on the board are not visible:
    for every row in the board:
      for every mole in the row:
        remove mole from all sprites
    
    draw winning screen
    
initialise pygame engine
initialise board
for every row in the board
  for every column in the board
    if random value is higher than our threshold
      initialise a Mole at the position
      add it into pygame sprites
      
while True:
  for each event received from pygame:
    if we placed a mole (check for left mouse button):
      get the position of the click on the board
      get the closest field there
      
      if the position is occupied by a mole:
        remove it
        
      check if we won
      if yes:
        show end game screen
      else:
        for neighbors around current mole:
          if neighbouring field is filled by a mole:
            remove it
          else:
            add a mole there
  
  check if we won
  redraw all changes
```
