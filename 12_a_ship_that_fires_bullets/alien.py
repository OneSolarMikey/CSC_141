import pygame
import random
from pygame.sprite import Sprite
from bullet import Bullet  # Import the Bullet class

class Alien(Sprite):
    '''A class to represent a single alien in the fleet'''
    
    def __init__(self, ai_game, row_index=0):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.row_index = row_index  # Track which row the alien belongs to
        
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (125, 75))
        self.rect = self.image.get_rect()
        
        # Position the alien based on its row.
        self.rect.x = 0  # Placeholder for actual X position
        self.rect.y = 0  # Placeholder for actual Y position
        
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if the alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

