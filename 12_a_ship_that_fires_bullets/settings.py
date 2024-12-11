class Settings:
    '''A class to store all settings for Alien Invasion'''

    def __init__(self):
        '''Initialize the game's settings'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.game_active = False

        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 250, 0)
        self.bullets_allowed = 10

        # Ship settings
        self.ship_speed = 3
        self.ship_width = 100
        self.ship_height = 100
        self.ship_limit = 3

        # Alien settings
        self.alien_speed = 3
        self.fleet_drop_speed = 15
        self.fleet_direction = 1
        self.alien_bullet_speed = 2

        # Wave settings
        self.wave = 1  # Start at wave 1
