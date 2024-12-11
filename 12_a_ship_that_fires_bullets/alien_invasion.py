import sys

import pygame
import random
import json
import pygame.mixer

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from background import Background
from stats import GameStats
from button import Button
from alien_bullet import AlienBullet

class AlienInvasion:
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        pygame.mixer.init()
        
        # Set up screen attributes
        self.settings = Settings()
        self.screen = pygame.display.set_mode((800, 600))
        self.settings.screen_width = 800
        self.settings.screen_height = 600
        pygame.display.set_caption("Alien Invasion")

        # Initialize game statistics
        self.stats = GameStats(self)

        self.leaderboard_file = "leaderboard.json"
        self.leaderboard = self._load_leaderboard()

        # Create button
        self.play_button = Button(self, "Play")
        self.leaderboard_button = Button(self, "Leaderboard")

        # Create the title screen
        self.title_font = pygame.font.SysFont(None, 72)

        self.shoot_sound = pygame.mixer.Sound('fire.mp3')
        self.ship_hit_sound = pygame.mixer.Sound('ship_hit.mp3')

        self._play_background_music()

        # Position the leaderboard button below the start button
        self.leaderboard_button.rect.top = self.play_button.rect.bottom + 20
        self.leaderboard_button.msg_image_rect.top = self.leaderboard_button.rect.top

        # Initialize other game elements
        self.background = Background(self.settings.screen_width, self.settings.screen_height, num_stars=200)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.alien_bullets = pygame.sprite.Group()

        self._create_fleet()
        self.clock = pygame.time.Clock()

        self.current_screen = "title"  # "title", "game", or "leaderboard"
        
        # Initialize bullet firing interval for aliens
        self.last_bullet_time = pygame.time.get_ticks()  # Track when aliens last fired
        self.bullet_interval = 1000  # Default firing interval (1 second)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.current_screen == "title":
                self._show_title_screen()
            elif self.current_screen == "leaderboard":
                self._show_leaderboard_screen()
            elif self.current_screen == "game":
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_alien_bullets()
                self.background.update()
                self._check_bullet_collisions()
                self._update_screen()

            self.clock.tick(60)

    def _play_background_music(self):
        """Load and play the background music."""
        pygame.mixer.music.load('bg_music.mp3')  # Path to your music file
        pygame.mixer.music.set_volume(0.5)  # Set the volume (0.0 to 1.0)
        pygame.mixer.music.play(-1, 0.0)  # Play the music in a loop (-1 means infinite loop)

    def _show_title_screen(self):
        """Show the title screen with the game title, Start button, and Leaderboard button."""
        self.screen.fill((0, 0, 0))  # Black background

        # Render the title text
        title_font = pygame.font.SysFont(None, 72)
        title_text = title_font.render("Alien Invasion", True, (255, 255, 255))  # White text
        title_rect = title_text.get_rect()
        title_rect.center = (self.settings.screen_width / 2, self.settings.screen_height / 3)
        self.screen.blit(title_text, title_rect)

        # Draw the buttons
        self.play_button.draw_button()
        self.leaderboard_button.draw_button()

        pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():  # Ensure 'event' is scoped correctly
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Properly placed inside the loop
                mouse_pos = pygame.mouse.get_pos()
                if self.current_screen == "title":
                    self._check_play_button(mouse_pos)
                    self._check_leaderboard_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        '''Start a new gaem when the player clicks play'''
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.current_screen = "game"

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

    def _check_leaderboard_button(self, mouse_pos):
        """Switch to the leaderboard screen when the Leaderboard button is clicked."""
        if self.leaderboard_button.rect.collidepoint(mouse_pos) and self.current_screen == "title":
            self.current_screen = "leaderboard"  # Switch to the leaderboard screen
    
    def _show_leaderboard_screen(self):
        """Show the leaderboard screen."""
        self.screen.fill((0, 0, 0))  # Black background

        # Render the leaderboard title
        title_font = pygame.font.SysFont(None, 72)
        title_text = title_font.render("Leaderboard", True, (255, 255, 255))
        title_rect = title_text.get_rect()
        title_rect.center = (self.settings.screen_width / 2, self.settings.screen_height / 6)
        self.screen.blit(title_text, title_rect)

        # Display leaderboard entries
        font = pygame.font.SysFont(None, 48)
        for i, (score, name) in enumerate(self.leaderboard):
            entry_text = f"{i + 1}. {name}: {score} pts"
            entry = font.render(entry_text, True, (255, 255, 255))
            self.screen.blit(entry, (self.settings.screen_width / 4, self.settings.screen_height / 4 + i * 50))

        pygame.display.flip()

        # Handle events for the leaderboard screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Escape key pressed
                    self.current_screen = "title"  # Go back to the title screen

    def _load_leaderboard(self):
        """Load the leaderboard from a file."""
        try:
            with open(self.leaderboard_file, "r") as f:
                return json.load(f)  # Load leaderboard data as a list of (score, name) tuples
        except FileNotFoundError:
            return []  # No file found, start with an empty leaderboard

    def _save_leaderboard(self):
        """Save the leaderboard to a file."""
        with open(self.leaderboard_file, "w") as f:
            json.dump(self.leaderboard, f)  # Save the leaderboard as JSON

    def _check_keydown_events(self, event):
        '''Respond to keypresses'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        '''Responf to key releases'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets group'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

            self.shoot_sound.play()

    def _alien_fire_bullet(self):
        """Allow one or two random aliens to fire bullets."""
        if self.stats.wave >= 3:  # Start firing bullets at wave 3
            # Randomly select 1 or 2 aliens to fire bullets
            num_firing_aliens = random.randint(1, 2)  # Choose either 1 or 2 aliens
            num_firing_aliens = min(num_firing_aliens, len(self.aliens.sprites()))  # Ensure no more aliens than available
            
            firing_aliens = random.sample(self.aliens.sprites(), k=num_firing_aliens)

            for alien in firing_aliens:
                bullet = AlienBullet(self, alien)
                self.alien_bullets.add(bullet)

    def _update_bullets(self):
        '''Update position of bullets and get rid of old bullets'''
        # Update bullet position
        self.bullets.update()

        # Get rid of the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0 or bullet.rect.top >= self.settings.screen_height:
                self.bullets.remove(bullet)

        # Check for bullet-alien collisions
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # Update score for each alien destroyed
        if collisions:
            for aliens in collisions.values():
                self.stats.score += 10 * len(aliens)  # Add 10 points for each alien destroyed

        # Check if all aliens are eliminated
        if not self.aliens:
            self.stats.wave += 1  # Increment the wave number
            self._pause_before_new_wave()  # Pause before creating a new wave
            self._create_fleet()  # Create a new fleet of aliens

    def _update_alien_bullets(self):
        """Update the position of alien bullets and check for collisions."""
        # Update bullet positions
        self.alien_bullets.update()

        # Check for collisions between alien bullets and the ship
        if pygame.sprite.spritecollideany(self.ship, self.alien_bullets):
            self._ship_hit()  # Handle ship being hit

        # Remove bullets that have gone off-screen
        for bullet in self.alien_bullets.copy():
            if bullet.rect.top >= self.settings.screen_height:
                self.alien_bullets.remove(bullet)
    def _check_bullet_collisions(self):
        """Check for collisions between bullets and targets."""
        # Check for collisions between player bullets and aliens
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # Update the score if aliens are hit
        if collisions:
            for aliens in collisions.values():
                self.stats.score += 10 * len(aliens)

        # Check if all aliens are eliminated
        if not self.aliens:
            self.stats.wave += 1  # Increment the wave number
            self._pause_before_new_wave()
            self._create_fleet()

    def _pause_before_new_wave(self):
        """Pause for a short time and display the wave number"""
        font = pygame.font.SysFont(None, 72)
        wave_text = f"Wave {self.stats.wave}"
        text = font.render(wave_text, True, (255, 255, 255))

        # Display the wave number in the center of the screen
        self.screen.fill(self.settings.bg_color)
        self.background.draw(self.screen)
        self.screen.blit(text, (self.settings.screen_width / 2 - text.get_width() / 2, self.settings.screen_height / 2))

        pygame.display.flip()

        # Pause for 2 seconds
        pygame.time.wait(2000)

    def _create_fleet(self):
        '''Create the fleet of aliens with multiple rows'''
        self.bullets.empty()
        self.alien_bullets.empty()

        self.ship.center_ship()

        # Create an alien to calculate the width and height
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        # Calculate the number of aliens that fit in a row
        available_space_x = self.settings.screen_width - (alien_width)
        number_aliens_x = available_space_x // (alien_width)

        # Calculate the number of rows of aliens that fit on the screen
        available_space_y = self.settings.screen_height - (2 * alien_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        '''Create an alien and place it in the fleet'''
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        alien.x = alien_width + alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + alien_height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()

        if self.stats.wave >= 12:
            self.settings.alien_speed = 5  # Set speed to 5 if wave is 12 or more
        elif self.stats.wave >= 6:
            self.settings.alien_speed = 4  # Set speed to 4 if wave is 6 or more but less than 9

        # Adjust the alien firing frequency after wave 9
        current_time = pygame.time.get_ticks()
        if self.stats.wave >= 9:  # After wave 9, aliens shoot more frequently
            self.bullet_interval = 1000  # Decrease interval to 1000ms for faster shooting
        else:
            self.bullet_interval = 1250  # Default interval of 1250ms

        # Fire alien bullets at the adjusted interval
        if current_time - self.last_bullet_time >= self.bullet_interval:
            self._alien_fire_bullet()
            self.last_bullet_time = current_time  # Update last bullet firing time

        self.aliens.update()
        self._check_alien_ship_collision()
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_alien_ship_collision(self):
        """Check if any aliens have collided with the ship."""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrease lives
            self.stats.ships_left -= 1

            self.ship_hit_sound.play()

            # Clear aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Recreate the fleet and reposition the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            pygame.time.delay(1000)
        else:
            self._game_over()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)  # Fill the background
        self.background.draw(self.screen)  # Draw the background

        if self.stats.game_active:
            self.ship.blitme()
            self.aliens.draw(self.screen)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            for bullet in self.alien_bullets.sprites():
                bullet.draw_bullet()

            # Draw score and lives during gameplay
            self._draw_score()
            self._draw_lives()
            self._draw_wave()

        else:
            # Redraw the button when the game is inactive
            self.play_button.draw_button()

        pygame.display.flip()  # Flip the screen to update it

    def _draw_score(self):
        """Display the score on the screen."""
        font = pygame.font.SysFont(None, 48)
        score_text = f"Score: {self.stats.score}"
        text = font.render(score_text, True, (255, 255, 255))
        self.screen.blit(text, (self.settings.screen_width - 190, 10))  # Display score at top-right corner

    def _draw_lives(self):
        """Display the number of lives left on the screen."""
        font = pygame.font.SysFont(None, 48)
        text = font.render(f"Lives: {self.stats.ships_left}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

    def _draw_wave(self):
        """Display the current wave number on the screen."""
        font = pygame.font.SysFont(None, 48)
        wave_text = f"Wave: {self.stats.wave}"
        text = font.render(wave_text, True, (255, 255, 255))  # White text
        self.screen.blit(text, (self.settings.screen_width - 475, 10))  # Display in top-right corner
    
    def _get_player_name(self):
        """Prompt the player to enter their name."""
        name = ""
        font = pygame.font.SysFont(None, 48)

        while True:
            self.screen.fill((0, 0, 0))  # Black background
            prompt_text = font.render("Enter your name: " + name, True, (255, 255, 255))
            self.screen.blit(prompt_text, (self.settings.screen_width / 6, self.settings.screen_height / 2))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return name
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode

    def _update_leaderboard(self, score, name):
        """Update the leaderboard with the new score and name."""
        self.leaderboard.append((score, name))
        self.leaderboard.sort(reverse=True, key=lambda x: x[0])  # Sort by score, descending
        self.leaderboard = self.leaderboard[:5]  # Keep only the top 5 entries
        self._save_leaderboard()  # Save the updated leaderboard to the file

    def _game_over(self):
        """Handle the end of the game."""
        print("Game Over!")
        name = self._get_player_name()
        self._update_leaderboard(self.stats.score, name)
        self.current_screen = "leaderboard"  # Switch to the leaderboard screen

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()