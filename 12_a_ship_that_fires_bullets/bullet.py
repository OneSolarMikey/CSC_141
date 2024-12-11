import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''A class to manage bullets fired from the ship or alien'''

    def __init__(self, ai_game, is_player_bullet=True, alien_rect=None):
        '''Create a bullet object at the ship's or alien's current position'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Set color based on whether it's a player bullet or alien bullet
        if is_player_bullet:
            self.color = self.settings.bullet_color  # Player bullet color
        else:
            self.color = (255, 0, 0)  # Red color for alien bullets

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        
        if is_player_bullet:
            self.rect.midtop = ai_game.ship.rect.midtop  # Player's bullet position
        elif alien_rect:
            self.rect.centerx = alien_rect.centerx  # Alien's bullet position
            self.rect.top = alien_rect.bottom  # Position it just below the alien's bottom

        # Store the bullet's position as a float
        self.y = float(self.rect.y)
        self.is_player_bullet = is_player_bullet

    def update(self):
        '''Move the bullet'''
        if self.is_player_bullet:
            self.y -= self.settings.bullet_speed  # Player's bullet moves up
        else:
            self.y += self.settings.bullet_speed  # Alien's bullet moves down

        self.rect.y = self.y

    def draw_bullet(self):
        '''Draw the bullet to the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)
