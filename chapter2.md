# Second Chapter: Advanced Python

##Functions 

## Classes

As we have seen in previous sections, Python allows us to store data (in variables) and also manipulate data (using functions). What we usually notice (especially when writing larger programs) is that some of our functions "go together" with some of the variables. For example, when making games, we often have code like the following:

    spaceship_position = (30, 270)
    spaceship_health = 100

    def move_spaceship(delta):
        spaceship_x, spaceship_y = spaceship_position
        delta_x, delta_y = delta
        
        spaceship_x += delta_x
        spaceship_y += delta_y
        
        spaceship_position = (spaceship_x, spaceship_y)

    def damage_spaceship(damage):
        spaceship_health -= damage
        
    if __name__ == '__main__':
        move_spaceship(10, -30)
        damage_spaceship(100)
    
In this code, the variables `spaceship_position` and `spaceship_health` are changed by the functions `move_spaceship` and `return_spaceship_to_base`, so they "go together". This is okay when we have only one spaceship, but it becomes hard to manage when we want to add additional ships.

Imagine if we had two spaceships. We would have variables for the position and health of each of them and we'd have to modify the functions `move_spaceship` and `damage_spaceship` so they change the appropriate variable. But then what if we now want three spaceships? We'd have to change everything again. It quickly becomes impractical.

To solve this problem, we introduce the idea of an **object**.
         
##Modules