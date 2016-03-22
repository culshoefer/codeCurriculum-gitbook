# Chapter 3: Programming Space Invaders with PyGame

We now know enough Python and we're finally able to start doing some proper game development. In this chapter, we are going to look at implementing one of the greatest computer games of all time: SPACE INVADERS!

#### Space Invaders Rules

1. The player can move left-right
2. Aliens move left-right as well, but not as often as the player
3. The player can shoot from time to time to take out the aliens and score points
4. The aliens shoot randomly and may harm the player (who has three lives)
5. The games ends if either all the aliens are dead or the player doesn't have any more lives
6. If you're lucky, a different kind of alien (a fast-moving one) can appear; killing it gives you loads of points

In this tutorial, we will only give you *pseudocode* – that is, code that looks almost like full-on code, but isn't actually Python (or any other programming language). You'll have to write the Python code itself, as the pseudocode only gives you the strucutre.

## Getting started

PyGame is a Python module (package) which implements a lot of the *boilerplate* code that are absolutely necessary for computer games (loading images, setting up GUI windows, drawing to screen, keeping track of time etc.), but are very boring to write. Using PyGame, we can concentrate on the fun parts: actually making games!

In PyGame, we use something called **sprites** and a **display**. We draw the sprites on the display (our screen). Let's start with some example code, straight from the [PyGame tutorial](http://www.pygame.org/docs/tut/intro/intro.html):

```python
import sys, pygame

pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  ballrect = ballrect.move(speed)

  if ballrect.left < 0 or ballrect.right > width:
    speed[0] = -speed[0]
  if ballrect.top < 0 or ballrect.bottom > height:
    speed[1] = -speed[1]

  screen.fill(black)
  screen.blit(ball, ballrect)
  pygame.display.flip()
```

Let's take this slowly. You might have noticed that we import `pygame` and then call functions belonging to it to change settings, load images etc. The [PyGame reference](http://www.pygame.org/docs/ref/pygame.html) is an invaluable resource – use it as often as you can.

Also notice the big `while` loop that seemingly goes forever. That's where everything in the game happens. And don't worry – the loop actually ends when the game receives the `pygame.QUIT` event (closing the window triggers this, for example)!

So how does PyGame draw stuff? Look at the last three lines: we first fill the screen black (to overwrite anything we drew previously and get a "blank slate"), then we draw the ball ([`blit`](http://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit) basically means "draw an image on top of another" – it takes two arguments: the image to be drawn, and the position where it should be drawn). Finallly, [`pygame.display.flip()`](http://www.pygame.org/docs/ref/display.html#pygame.display.flip) updates the content of the entire display with what's now in our screen object.

If we did not have the flip function, we would be unable to see our changes. Since it is very expensive to update the display, it is better to pile up a lot of changes in a `screen` object and then call `flip()` on the display only once to set them free.

## Creating PyGame classes: `Entity`

![The video game classic](img/space_invaders.png) Let's start by writing an `Entity` class that is responsible for one, *well*, entity (aliens, the player, the super-alien). It has the following attributes:

```python
x, y    # the entity's position as coordinates
dx, dy  # the change in coordinates in one update
image   # the image of the entity
width, height   # width and height of the entity
rect    # stores the "bounding box" of the entity
posBoundaryLeft, posBoundaryRight   # boundaries the entity is restricted to
consider    # whether we actually draw the entity or not
gameWidth, gameHeight   # for orientation the game's width and height.
```
The following is the constructor for class `Entity`:
```python
def __init__(self, x, y, dx, dy, image, gameWidth, gameHeight):
    super(Entity, self).__init__()

    self.x = x
    self.y = y
    self.dx = dx
    self.dy = dy

    self.image = pygame.image.load(image)
    self.width = self.image.get_width()
    self.height= self.image.get_height()

    self.rect = self.image.get_rect()
    self.rect.x = self.x
    self.rect.y = self.y

    self.posBoundaryLeft = 20 + self.width/2
    self.posBoundaryRight= gameWidth - (20 + self.width/2)

    self.consider = True

    self.gameWidth = gameWidth
    self.gameHeight = gameHeight
```

OK, so far so good. Let's continue!

As you can see, `posBoundaryLeft` and `posBoundaryRight` are by default set to be 20 pixels from the edges of the screen plus half of the `Entity`'s width. Go to the PyGame example at the beginning of this chapter (the one with the ball) and rewrite it to use the `Entity` class.

We need to add a few more methods. Please fill in the blanks as necessary:

```python
def update(self):
  '''this is just a function to both move the entity,
  check for its boundaries and to set
  self.rect.center = (self.x, self.y),
  in other words to adjust the rect to the entity's position'''

def intersects(self, entity):
  #return self.rect.colliderect(Rect of another entity)
  '''this is a function that is built-in by default,
  but it is not elegant. So we write a nicer version.
  This checks if the rect of one entity collides with another'''

def move(self):
  #adds dx to the variable x of the object and dy to y

def checkBoundaries(self):
  if self.x < self.posBoundaryLeft:
    self.x = self.posBoundaryLeft
    self.dx = - self.dx

  '''checks if the position is too far left:
  Is x smaller than posBoundaryLeft?
  If so, set the position of the object to the boundary
  and revert the direction in x-dimension (dx),
  **similarly for the right side! Fill in this part!**'''

def isInScreen(self):
  #return true if it is in screen (within game dimensions)
  '''almost the same like the intersects function above,
  just checks if both entities are considered or not'''

def isHit(self, entity):
  '''return True if we consider the object,
  and if we consider the other entity and they intersect.
  In all other cases, return False'''

def draw(self, screen):
  '''if to consider the object and it is inscreen then
    call screen.blit on the objects image and its rect'''
```
#### Exercise: ball collision

With this new class, write a small game in which we have two balls. Use the example code at the beginning of the chapter and start shaping it with our newly-made `Entity` class. If the balls collide, print "Oh no!" on the screen.

## Giving life to `Entity`: `AliveEntity`

Well, that's all nice and fine, but I want a game!

What do we do when we need to add some new kind of object that builds upon an already existing kind? It's simple. We create a new class and **inherit** from the existing one. Let's do that now.

From our `Entity` class, let's create a new class called `AliveEntity`. Since we have two kinds of entities (some that need scores and some that don't), we need to have two separate classes for them. Even though we aren't adding that much new stuff, we still need to create a new, different class. Here is a skeleton for the `AliveEntity` class, including the constructor:

```python
class AliveEntity(Entity):
    def __init__(self, score, x, y, dx, dy, image, lives, gameWidth, gameHeight):
        super(AliveEntity, self).__init__(x, y, dx, dy, image, gameWidth, gameHeight)
        self.score = score
        self.lives = lives
```

Why should we do that, you ask? Bare with me for a moment. Since we have a new class inheriting from the old one, we can now **override** the `update()` method:

For aliens, we don't want them to move around too often, so we need one method where the objects update without moving, and one method where they update AND where they move.

Additionally, we also check if the entity has any lives left. If it doesn't, we simply don't consider the entity.

Lastly, we add an option to remove a life (this might seem superfluous now, but it will help us focus on the more important bits later on).

Here's the rest of the pseudocode for AliveEntity, for you to fill in:

```python
 def update(self):
   check boundaries of objects
   set the object's rectangle to the position (like above)
   if it is not in screen or if it has less than zero lives,
    do not consider the entity

def updateWithMove(self):
    update
    move

def removeLife(self):
    subtract 1 from lives
```

 ...that's it! Now, up for an exercise:

##### Exercise: displaying an array of entities

Create a multidimensional array of `AliveEntity`s. In a new file called `spaceinvaders.py`, import PyGame and the new class:

```python
import pygame
from AliveEntity import AliveEntity
```

and then create said array. Each element of the array should be an entity. Download any image you like from the Internet to represent the entities, or just use [this one](img/special_alien.png). The goal of this exercise is to display the entities on screen in a grid-like fashion. See the picture below for help.

![Array indeces](img/array_indeces.png)

The "lowest" element should be on the top-left, then right to it, [0][1]... etc. In order to do this, create two for-loops: the first one just goes through all the "rows", the second one through all the elements in that row.

Make sure that you position the elements correctly, with enough spacing. For drawing, just loop through the entire array, calling `draw()` on each element.

Here's some skeleton code for you to modify:

```python
def createAliens(cols, rows):
    aliens = []
    for i in range(cols):
        row = []
        for j in range(rows):
            newAlien = AliveEntity... create object in the right way
            row.append(newAlien)
        aliens.append(row)
    return aliens

def drawAliens(self, aliens):
    for row in aliens:
        for alien in row:
            if alien is not None:
                alien.draw
```

## PyGame keyboard input and the `Player` class

Now, let's create the class representing the player. Why do we need a special class for the player, you ask? Well, the player has some special responsibilities (that simple `AliveEntity` objects don't have):

* If the user presses the left key, the player moves left
* If the user presses the right key, the player moves right
* Each time the player updates, it has to reset its speed to 0, if no button is pressed

These functions will be implemented in separate methods. Obviously, `Player` inherits from `AliveEntity`. Here's a skeleton of the `Player` class:

```python
import pygame
from AliveEntity import AliveEntity

class Player(AliveEntity):
    def __init__(self, score, lives, gameWidth, gameHeight):
        super(Player, self).__init__(score, gameWidth/2, 400, 0, 0, "img/player.png", lives, gameWidth, gameHeight)

    def checkKeyboardInput(self, pressed_keys):
        self.checkGoLeft(pressed_keys)
        self.checkGoRight(pressed_keys)

    def checkGoLeft(self, pressed_keys):
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            set dx to -1

    def checkGoRight(self, pressed_keys):
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            set dx to one

    def update(self):
        call the update function of the super class
        move the player
        set dx to zero
```

## The `Game` class: the main access point to our game

Now, let's create the main class of our game, logically called `Game`. In here, all the basic functionality is carried out:

 * We draw all of our entities
 * We process input
 * We see if the game is over
 * We carry out all the other game rules

So, for this, create a new file called (you wouldn't have guessed) `Game.py`.

Here's a skeleton for the file:
```python

import pygame, random
from AliveEntity import AliveEntity

class Game():
    def __init__(self, startScore, aliens, player, width, height, size):
        self.score = startScore
        self.ticks = 0
        self.player = player
        self.aliens = aliens
        self.running = True
        self.aliensExist = True
        self.screen = pygame.display.set_mode(size)
        self.width = width
        self.height = height

    def addScore(self, toAdd):
        add the amount there to the score

    def isLucky(self, chance):
        see if random.random() is greater than change, If you want to find out what random.random() does, google it!

    def checkGameStop(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def computeInput(self):
        for event in pygame.event.get():
            self.checkGameStop(event)

    def drawAlien(self, alien):
        if self.ticks % 200 == 0:
          update the alien and move it
        else:
            just update it
        in any case, draw the alien

    def drawAliens(self):
        self.aliensExist = False
        loop through all the aliens, just as described in the exercise before.
        for each alien, decide:
          If alien is not None:
            self.aliensExist = True
            self.drawAlien(alien)

    def update(self):
        self.player.draw(self.screen)
        self.drawAliens()
        self.computeInput()
        self.player.update()
        self.ticks += 1
        if self.isGameOver():
            self.running = False

    def isGameOver(self):
        return true if the player doesnt have any more lives or if there are no more aliens

    def isRunning(self):
        return self.running
```

Please complete the code accordingly.

In order to use this game, we expand our `spaceinvaders.py` file a bit.

```python
import pygame
import sys
from AliveEntity import AliveEntity
from Player import Player
from Game import Game

pygame.init()

size = width, height = 448, 512
white = 255, 255, 255

def spawnNewAlien(xpos, ypos):
    startPosx = width/2 -1400 + 30 * xpos
    startPosy = height/2 - 130 + 30 * ypos
    imageName = "img/sprite" + str(ypos + 1) + ".png"
    score = 5 * (6 - ypos)
    newAlien = AliveEntity(score, startPosx, startPosy, 4, 0, imageName, 1, width, height)
    newAlien.posBoundaryLeft = 50 + 30 * xpos
    newAlien.posBoundaryRight= width -50 - 30 * (10 - xpos)
    return newAlien

def createAliens(cols, rows):
    here the code for creating the array of aliens. For every alien, it should create the alien and add it to the array. We do this to pass the array to our Game class later. The code below should look similar to the one above, except for one point:
    aliens = []
    for i in range(cols):
        row = []
        for j in range(rows):
            newAlien = spawnNewAlien(i, j)
            row.append(newAlien)
        aliens.append(row)
    return aliens

def printEndMessage(message):
    text = game.display.font.render(message, 1, white)
    textRect = text.get_rect()
    textRect.x = width/2
    textRect.y = height/2
    game.screen.blit(text, textRect)
    pygame.display.flip()

def runGame(game, clock):
    while game is running,
      call game.update()
      do pygame.display.flip()
      clock.tick(300)

clock = pygame.time.Clock()
aliens = createAliens(11, 5) #we create 11x5 = 55 aliens
player = Player(-100, 3, width, height) #the player is a special class.
game = Game(0, aliens, player, width, height, size)

runGame(game, clock)

print("END")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_SPACE]:
        break
    if no aliens exist,
        printEndMessage("YOU WON!")
    else:
        printEndMessage("YOU LOST.")
    clock.tick(300)
pygame.quit()
```

You see the part after `print("END")`? This part just displays a nice end message to the user. Feel free to customize anything.

## Adding randomness

If you've read the description carefully, you remember that we want an alien to appear every once in a while and to sweep right at a high speed (the so-called special alien). For this to happen, we need to add some things to our `Game` class:

In our constructor, we add:

```python
self.specialAlien = AliveEntity(0, 0, 0, 0, 0, "img/shot.png", 0, width, height)
self.specialAlien.consider = False
```

Further down in the code, let's add one more method:

```python
def spawnSpecialAlien(self):
  self.specialAlien = AliveEntity(100, 100, 90, 2, 0, "img/sprite8.png", 1, self.width, self.height)
  self.specialAlien.posBoundaryRight = self.width + 40
```

In this method, we just set the instance variable to a new entity with the following properties:

```
score: 100
position x: 100
position y: 90
dx: 2
dy: 0
image: "img/sprite8.png"
lives: 1
width: width of game
height: height of game
```

Easy! In addition to that, if the alien moves further right than `width + 40`, will it stop? Yes, according to how we specified in our AliveEntity class, as soon as it goes out of bounds.

As you can see, this is quite basic here. Because we've done all the hard work already, now we just need to fill in the blanks.

Create a function in our `Game` class that combines both functions:

```python
def dealWithSpecialAlien():
  self.specialAlien.updateWithMove()
  self.specialAlien.draw()
```

In our `update()` function, we have to call `dealWithSpecialAlien()` after we draw the player.

One last thing: so far, we don't add the special alien at all. To adjust this, we add more code at the end of our `update()` function to call our `spawnSpecialAlien()` function if we are lucky. Let's do this. Add:

```python
if(self.isLucky(0.99999)):
    self.spawnSpecialAlien()
```

Done! Feel free to set the value in parentheses to a lower value, if you want the special alien to spawn more often.

## Shooting!

Let's start with the following rules:

* The player can fire shots which can hit aliens and destroy them
* The aliens randomly shoot at the player and can reduce the amount of lives the player has

For this, we don't need a whole class to encapsulate a shot.
It is enough that we just use our existing `Entity` class. Convenient!

### Making the player shoot

In our player class, let's add a couple of functions.

1. We have to account for shooting quickly: we only want the player to be able to shoot, say, every 200 ticks, so we have to keep track of the previous shot. We do so by adding a simple instance variable in the `Player` class. To our constructor, add:

```python
self.last_shot = 0
```

2. We need a separate function to check if the player is shooting. Two conditions need to be met: the spacebar key has to be pressed and the time passed since the last shot should be at least 200 ticks. This gives us:

```
def checkShoot(self, pressed_keys, ticks):
  shot = None
  if pressed_keys[pygame.K_SPACE] and ticks > self.last_shot + 200
    create shot
  return shot
```

For now, just replace `create shot` with `print("Shooting!")` to check that your code works correctly.

3. Add the code for creating a shot. This means we create two functions: one for all of the shooting logic (`shoot()`) and one for actually creating the shot (`makeShot()`). For `shoot`, the function should look like this (complete the blanks):

```python
def shoot(self, ticks):
  shot = self.makeShot()
  set last shot to the ticks specified
  return shot
```

We want to specify the shot:

```
x position: self.x
y position: self.y
dx: 0
dy: -1.25
image: "img/shot.png"
width: self.gameWidth
height: self.gameHeight
```
Now, we can write the `makeShot()` function. If you can figure it out yourself, please don't look at the code below!

```python
def makeShot(self):
  shot = Entity(self.x, self.y, 0, -1.25, "img/shot.png", self.gameWidth, self.gameHeight)
  return shot
```
Back in our `checkShoot()` function, we can now call the `shoot()` function with the correct arguments. Change your code to do so.

**ONE MORE THING, THOUGH!**

In the `Game` class, in the `computeInput()` function, at the bottom, add:

```python
shot = self.player.checkShoot(pressed_keys, self.ticks)
```
... to make shooting work.

### Making the aliens shoot

This is some serious business, when aliens shoot. Let's create a class for it. Since this won't be the only time that we have to perform functions on the shots, we just summarise it as `ShotEngine`. The class (including imports) looks like this (again, fill in the blanks!):

```python
import pygame
import random
from Entity import Entity

class ShotEngine():
    def __init__(self, gameWidth, gameHeight):
        self.alienShots = []
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight

    def isLucky(self, chance):
        return random.random() > chance

    def doesAlienShoot(self):
        return self.isLucky(0.997)

    def makeShot(self, x, y, speed):
        shot = Entity(x, y, 0, speed, "img/shot.png", self.gameWidth, self.gameHeight)
        return shot

    def addAlienShot(self, x, y):
        shot = self.makeShot(x, y, 0.75)
        self.alienShots.append(shot)

    def deleteAlienShot(self, shot):
        self.alienShots.remove(shot)

    def makeRandomShots(self, aliens):
        if(alien does shoot):
            row = random.randint(0, 4)
            col = random.randint(0, 10)
            while not aliens[col][row].consider: #skip aliens that are not visible
                row = random.randint(0, 4)
                col = random.randint(0, 10)
            x = aliens[col][row].x
            y = aliens[col][row].y
            add alienshot to (x,y)

    def considerAlienShot(self, shot, player):
        score = 0
        if player is hit by shot:
          self.alienShots.remove(shot)
          remove life from player
          add score of player to the score
        return score

    def computeAlienShots(self, player):
        score = 0
        for shot in self.alienShots:
            score += self.considerAlienShot(shot, player)
        return score

    def drawAlienShots(self, screen):
        for shot in self.alienShots:
            if not shot.isInScreen():
                self.deleteAlienShot(shot)
            else:
                shot.update()
                shot.draw(screen)

    def computeShots(self, player, specialAlien, aliens):
        score += self.computeAlienShots(player)
        return score

    def update(self, aliens, screen):
        make random shots
        draw alien shots on screen
```

Back in our `Game` class, we just add the following line in the constructor:
```python
self.shotEngine = ShotEngine(width, height)
```

Now that we are done with shooting, let's finalise our game. We now only need to:

* Display the current score of the game
* Display the amount of lives the player has

For this, we create a last class called `Display`. Here is the skeleton for its file:

```python
import pygame, copy

topDist = 150
liveXDist = 30
white = 255, 255, 255
black = 0, 0, 0

class Display():
    def __init__():
        self.lifeImage = pygame.image.load("img/heart.png")
        self.font = pygame.font.SysFont("monospace", 20)
        self.text = self.font.render("SCORE", 1, white)
        self.textpos = self.text.get_rect()
        self.textpos.x = 20
        self.textpos.y = 30
        self.scorepos = copy.copy(self.textpos)
        self.scorepos.x = self.scorepos.x + self.text.get_width() + 20
        self.scorepos.y = self.scorepos.y
```

Because pygame is weird, we need to carefully store the font in a separate instance variable. Similarly for the positions of the text.

Now, let's add a function to draw all of the text, given the current score of the game and a screen to render it onto:

```python
    def drawAllText(self, screen, score):
        screen.fill(black)
        screen.blit(self.font.render(`self.score`, 30, white), self.scorepos)
        screen.blit(self.text, self.textpos)
```

... and likewise a function to draw the lives the player has:

```python
    def drawLives(self, screen, numLives):
        for i in range(numLives):
            livesRect = self.lifeImage.get_rect()
            livesRect.x = self.textpos.x + topDist + i * liveXDist
            livesRect.y = self.textpos.y
            screen.blit(self.lifeImage, livesRect)    
```

Finally, we add a function to call both drawing functions together. Fill in the rest:

```python

    def drawAll(self, screen, score, numLives):
        draw all text
        draw lives
```

Finally, in our `Game` class, we add the instance variable for `Display` in our constructor:

```python
self.display = Display()
```

In the `update` function, we add:

```python
self.display.drawAll(screen, score, self.lives)
```

And we're done! Congratulations, you just implemented Space Invaders!
