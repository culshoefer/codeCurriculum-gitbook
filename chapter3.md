# Third Chapter: Programming games in PyGame

##Space invaders!
Now, let's start with proper game development, shall we? Let's start with one of the greatest games ever invented: SPACE INVADERS!
In practice, we have the following rules:
1) The player can move from left to right
2) Aliens move from right to left as well but not as often as the player
3) The player can shoot from time to time to take out the aliens and score points
4) The aliens shoot randomly and may harm the player (who has three lives)
5) The game ends if either no aliens are present any more or the player doesn't have any lives
6) If you're lucky, a different kind of alien can appear, moving fast but earning you loads of points

##So how do we start?
In this tutorial, I will only provide you with so-called *pseudocode*, that is code that looks almost like full-on code, but you have to do all the coding yourself. We have done all the thinking for you.

Let me first explain a bit how PyGame works.
In PyGame, we use something called **sprites** and a **display**. We draw sprites on the display (our screen).
Let's start with some example code:
```python
#from http://www.pygame.org/docs/tut/intro/intro.html, yes I know shamelessly copied
import sys, pygame

pygame.init()
size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()
while 1:
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
A couple of things here. You might have noticed that there is a `pygame` object which we modify, when we load images etc. Also notice the big `while`-loop, that goes forever (seemingly). So how does pygame draw stuff? Look at the last three lines: We first fill the screen black, then we draw the ball (`blit` is a very weird function, just be fine with passing the image and its rectangle and position to it). Finally, the `flip()` method: This finally accepts all changes and presents them to the viewer.

If we did not have the flip function, we would be unable to see our changes. Since it is very expensive to always draw stuff on the screen, it is better to have a lot of changes and then call `flip()` only once to set them free.

##Our first class for space invaders
![The video game classic](img/space_invaders.png)
We start with a **Entity** class, that is responsible for one, well, entity (so aliens, player...).
It has the following attributes:
```python
x, y, #the entities position as coordinates
dx, dy, #the change in coordinates in one update
image, #the image of the entity
width, height, #width and height of the entity
rect, #just an instance variable for the rect of the image, because we need that quite often
posBoundaryLeft, posBoundaryRight, #left and right boundaries in which the entity is restricted to move in


consider, #whether we actually draw the entity or not
gameWidth, gameHeight #for orientation the game's width and height.
```
The following is the constructor for class `Entity`:
```python
def __init__(self, x, y, dx, dy, image, gameWidth, gameHeight):
b        super(Entity, self).__init__()
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
Ok, so far so good, don't leave me just yet! As you can see, posBoundaryLeft and posBoundaryRight are by default set to be 20 pixels from the edges of the screen (plus half of the Entity's width). Please do go to the PyGame example and rewrite it using the Entity class. There, we will now add more methods:
```python
def update(self):
  '''this is just a function to both move the entity, check for its boundaries and to set self.rect.center = (self.x, self.y), in other words to adjust the rect to the entity's position'''

def intersects(self, entity):
  return self.rect.colliderect(Rect of another entity)
  '''this is a function that is built-in by default, but not so elegantly. This checks if the rect of one entity collides with another'''

def move(self):
  #adds dx to the variable x of the object and dy to y

def checkBoundaries(self):
  if self.x < self.posBoundaryLeft:
    self.x = self.posBoundaryLeft
    self.dx = - self.dx
  '''checks if the position is too far left: Is x smaller than posBoundaryLeft? If so, set the position of the object to the boundary and revert the direction in x-dimension (dx), similarly for the right side!'''

def isInScreen(self):
  return True if y > 0 and x > 0 and y < gameheight and x < gamewidth
  #return true if it is in screen (within game dimensions)

'''almost the same like the intersects function above, just checks if both entities are considered or not'''
def isHit(self, entity):
        return self.consider and entity.consider and self.intersects(entity)

def draw(self, screen):
  if to consider the object and it is inscreen then
    call screen.blit on the objects image and its rect
```
###Exercise time!
With this new class, start writing a small game in which we have two balls. For this, use the example code above and start shaping it with our fresh Entity class. If the two balls should collide, print "Oh no!" on the screen!

##Well, that's nice and fine, but I want a game!
Don't worry just for now! Let's add ANOTHER class, just for the sake of it to **inherit** from our Entity class, let's call it AliveEntity. Since we have both entities that need scores and those which don't, we need two separate classes for them. Although we essentially don't add much more to it, we still need different classes. Here is the constructor of `AliveEntity`:
```python
class AliveEntity(Entity):
    def __init__(self, score, x, y, dx, dy, image, lives, gameWidth, gameHeight):
        super(AliveEntity, self).__init__(x, y, dx, dy, image, gameWidth, gameHeight)
        self.score = score
        self.lives = lives
```
If you know say "wow that is weird", just bare with me one more moment. Because now, we can **overwrite** the `update()` method from the `Entity` class:
