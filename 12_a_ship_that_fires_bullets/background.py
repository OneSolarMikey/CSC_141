import pygame
import random

class Background:
    def __init__(self, screen_width, screen_height, num_stars):
        '''Initialize the background with stars'''
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.num_stars = num_stars
        self.stars = self._generate_stars()

    def _generate_stars(self):
        '''Generate a list of random stars'''
        stars = []
        for _ in range(self.num_stars):
            star_x = random.randint(0, self.screen_width - 1)
            star_y = random.randint(0, self.screen_height - 1)
            star_size = random.choice([2, 3, 4])
            star_speed = random.uniform(0.5, 2.0)
            stars.append({"x": star_x, "y": star_y, "size": star_size, "speed": star_speed})
        return stars
    
    def update(self):
        for star in self.stars:
            star["y"] += star["speed"]
            if star["y"] > self.screen_height:
                star["y"] = 0
                star["x"] = random.randint(0, self.screen_width - 1)
    
    def draw(self, screen):
        '''Draw the stars onto the screen'''
        for star in self.stars:
            pygame.draw.rect(screen, (255, 255, 255), (star["x"], star["y"], star["size"], star["size"]))