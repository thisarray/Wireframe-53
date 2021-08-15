def draw(screen, frame):
    screen.blit("background_1",(800-frame%(800*8)/4,0))
    screen.blit("background_0",(800-(frame+800*4)%(800*8)/4,0))
