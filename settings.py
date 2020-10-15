class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)


        #ship settings 
        #self.ship_speed = 1.5
        self.ship_limit = 3


        #bulletr settings
        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #alien settings
        
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left
        

        #How quicly the game sppeds up
        self.speedup_scale = 1.1

        #How quicly the game speeds up
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Initialize settings that change throuout the game'''
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0


        #fleet_direction of represents right; -1 represents left
        self.fleet_direction =1

        #SCORING
        self.alien_points = 50 

    def increase_speed(self):
        '''Increase speed settings and alien point values'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale


        self.alien_points = int(self.alien_points * self.score_scale)
        

