import pygame

# import Classes
from EVA_Class import EVA
from Master_Class import Master
from Station_Class import Station

width, height = 600, 600


def main():
    # setup pygame
    pygame.init()
    #print('hi')
    pygame.display.set_caption("EVA Simulation")
    win = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    fps = 10

    # setup objects
    charge = Station(width, height, win)
    me = Master(width, height, win)
    eva = EVA(width, height, win, charge, me)

    win = pygame.display.set_mode((width, height))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # draw state
        
        charge.draw()
        eva.run()
        me.draw()
        pygame.display.update()

        win.fill(0)
        clock.tick(fps)
    pygame.quit()


if __name__ == '__main__':
    main()
