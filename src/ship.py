import pygame 
from pygame.sprite import Sprite
#In Pygame, the origin (0,0 is at the top left corner of the screen)
#Coordinates increase as you go down and to the right 
#Bottom right is 1200 x 800

class Ship(Sprite): 
    """A class to manage the ship."""

    def __init__(self, ai_game): 
        """Initialize the ship and set its starting position"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings 
        self.screen_rect = ai_game.screen.get_rect() 

        # Load the ship image and get its rect. 
        self.image = pygame.image.load('images/space-ship-3-icon.bmp')
        self.rect = self.image.get_rect() 

        # Start each new ship at the bottom center of the screen. 
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position 
        self.x = float(self.rect.x) 

        # Movement flag 
        self.moving_right = False 
        self.moving_left = False 


    def update(self): 
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect. 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
    
    
    def blitme(self): 
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) 


    def center_ship(self): 
        self.rect.midbottom = self.screen_rect.midbottom 
        self.x = float(self.rect.x) 
