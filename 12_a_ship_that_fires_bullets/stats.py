class GameStats:
    '''Track statistics for Alien Invasion'''

    def __init__(self, ai_game):
        '''Initialize statistics'''
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        
        # Add a new attribute for the wave
        self.wave = 1  # Start at wave 1
        self.ships_left = self.settings.ship_limit

    def reset_stats(self):
        '''Reset statistics that can change during the game'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.wave = 1
