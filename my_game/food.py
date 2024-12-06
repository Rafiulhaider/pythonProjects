import pygame as py

class Foods:
    def __init__(self, Screen):
        
       
        self.screen = Screen;
        self.color = 'red';
        self.width_food = 10
        self.height_food = 10
        
    
    def draw_food(self):
        
        py.draw.rect(self.screen, self.color, (self.screen.get_width()/2, self.screen.get_height()/2, self.width_food, self.height_food));
        
        
        
        
    
    
        pass