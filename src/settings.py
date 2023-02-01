class Settings: 
    """A class to store all settings for Alien Invasion."""

    def __init__(self): 
        """Initialize the game's settings"""
        #Screen Settings 
        self.screen_width = 1200   # sets width for window
        self.screen_height = 800   # sets height for window
        self.bg_color = (0, 0, 0)  # sets background for window

       
        # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 255, 0) 
        self.bullets_allowed = 3

    
        self.fleet_drop_speed = 10 
        self.speedup_scale = 1.1 
        self.score_scale = 1.5 
        self.initialize_dynamic_settings() 


    def update(self): 
        self.x += self.settings.alien_speed
        self.rect.x = self.x 

    
    def initialize_dynamic_settings(self): 
         # Ship settings 
        self.ship_speed = 1.5
        self.ship_limit = 3
        self.alien_speed = 1.0 

        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        self.alien_points = 50 


    def increase_speed(self): 
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points) 

        