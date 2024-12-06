import pygame as py
from wall import walls
from food import Foods

py.init()

screen = py.display.set_mode((800, 600))
clock = py.time.Clock()
blink = 500
last_toggle = py.time.get_ticks();
food_visible=True;

running = True
wall_instances = walls(screen)
food_instance = Foods(screen)
while running:
    
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
    
    current_time = py.time.get_ticks()
    
    if current_time - last_toggle > blink:
        food_visible = not food_visible
        last_toggle=current_time;
        
    
    
    screen.fill('BLACK')
    
    wall_instances.draw()
    
    if food_visible:
        food_instance.draw_food()
    
    py.display.flip()
    
    clock.tick(60)
py.quit()