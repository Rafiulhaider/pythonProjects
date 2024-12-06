import pygame as py

class walls:
    def __init__(self, Screen , color = 'blue', thickness =10):
        
        self.screen = Screen
        self.screen_width = Screen.get_width();
        self.screen_height = Screen.get_height();
        
        self.color = color
        self.thickness = thickness
        
    def draw(self):
        
        
        
        py.draw.rect(self.screen, self.color,(0,0, self.screen_width, self.thickness))
        py.draw.rect(self.screen, self.color,(0,0, self.thickness, self.screen_height))
        py.draw.rect(self.screen, self.color, (0,self.screen_height-self.thickness,self.screen_width, self.thickness ))
        py.draw.rect(self.screen, self.color, (self.screen_width-self.thickness, 0,self.thickness, self.screen_height))
        
    
        
        
    
    
    



