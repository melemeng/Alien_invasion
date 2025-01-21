
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
        self.alien = Alien(self)
        

           


    def _check_events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right 
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):

        #redraw the screnn during each pass through the loop

        self.screen.fill(self.settings.bg_color)
            
        self.ship.blitme()
        self.alien.blitme()
        # Make the most recently drawn screen visible
        pygame.display.flip()




    def run_game(self): 
        
        """ Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse event.
            self._check_events()
            self.ship.update()
            self._update_screen()
          
                
class Settings:

    # A class to store all settings for Alien AlienInvasion
    
    def __init__(self):
        
        """ Initialize the games settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color      = (135, 206, 235)
        #Ship settings
        self.ship_speed = 1.5




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
        

         #Movement flag
        self.moving_right = False
        self.moving_left = False
        
        self.settings = ai_game.settings

        #Store a decimal value for the ships horizontal position
        self.x = float(self.rect.x)
   

    def blitme(self):
        """drawn the shit at its current location"""

        self.screen.blit(self.image, self.rect)

    def update(self):
        """ update the ships position bases onthe movement of flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0 :
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
 

class Alien:
    """ A class to manage the Alien Ship """

    def __init__(self, ai_game):
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/alien.bmp')
        
        self.new_width = 80 
        self.new_height = 60

        self.image = pygame.transform.scale(self.image, (self.new_width,self.new_height))
        
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center


    def blitme(self): 
        """ draw the Alien at its current location"""

        self.screen.blit(self.image, self.rect)







if __name__ == '__main__':
    
    # game instance , and run game 
    ai = AlienInvasion()
    ai.run_game()

