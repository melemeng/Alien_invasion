
import sys

import pygame

class AlienInvasion:
    
    def __init__(self):
        
        #pygame setup
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
    
    def run_game(self): 
        
        """ Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse event.
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

           
            #redraw the screnn during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            
            self.ship.blitme()
            # Make the most recently drawn screen visible
            pygame.display.flip()

    
class Settings:

    # A class to store all settings for Alien AlienInvasion
    
    def __init__(self):
        
        """ Initialize the games settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color      = (230, 230, 230)


class Ship:
    """ A class to manage the ship """

    def __init__(self, ai_game):
        #Initialize the ship set to its starting position

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

    

        # Load the Ship image and get its screen_rect
        self.image = pygame.image.load('images/rocket.bmp')

        # Ship dimension 
        self.new_width = 90 
        self.new_height = 70 

        self.image = pygame.transform.scale(self.image, (self.new_width,self.new_height))

        self.rect  = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """drawn the shit at its current location"""

        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    
    # game instance , and run game 
    ai = AlienInvasion()
    ai.run_game()

