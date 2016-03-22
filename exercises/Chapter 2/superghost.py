import pygame
from .character import NUM_DIRECTIONS
from .ghost import Ghost
import random

NUM_MODES = 3
CHASE_MODE = 0
SCATTER_MODE = 1
FRIGHTENED_MODE = 2

class SuperGhost(Ghost):
    def __init__(self, level, normal_image, frightened_image, scale_factor, arena_position, direction, speed):
        Ghost.__init__(self, level, normal_image, frightened_image, scale_factor, arena_position, direction, speed)

    def _frightened(self):
        self.curr_direction = random.randint(0, NUM_DIRECTIONS - 1)


    ############################
    # Change these two methods #
    ############################

    def frighten(self):
        self.mode = FRIGHTENED_MODE
        self.frightened_at_time = pygame.time.get_ticks()
        self.speed *= 0.25
        self.image = self.frightened_image

    def handle_collision(self):
        if self.mode == FRIGHTENED_MODE:
            print "You ate {}".format(self.name)
            self.respawn()
            return False
        else:
            print "You were eaten by {}.".format(self.name)
            return True

