
import sys

import pygame

class AlienInvasion:
    
    def __init__(self):
        
        #pygame setup
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
        self.bg_color = (230, 230, 230)

    
    def run_game(self): 
        
        """ Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse event.
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

           
            #redraw the screnn during each pass through the loop
            self.screen.fill(self.bg_color)
            # Make the most recently drawn screen visible
            pygame.display.flip()

    




if __name__ == '__main__':
    
    # game instance , and run game 
    ai = AlienInvasion()
    ai.run_game()

