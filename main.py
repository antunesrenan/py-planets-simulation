import pygame
import math

pygame.init()

#program window (win) size
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#planet colors
WHITE = (255, 255, 255)
BEGE = (245, 245, 220)
YELLOW = (255, 255, 0)
BLUE = (100,149,235)
RED = (188, 39, 50)
GREY = (80, 80, 80)

pygame.display.set_caption("Planet Simulation")

#planet size
SUNMASS = 1.98892 * 10**30
MERCMASS = 3.30 * 10**23
VENUSMASS = 4.8685 * 10**24
EARTHMASS = 5.9742 * 10**24
MARSMASS = 6.39 * 10**23

class Planet:
    #astronomical unit in meters
    AU = 149.6e6 * 1000

    #gravitational constant
    G = 6.67428e-11

    #defining the scale for 1 AU = 100px
    SCALE = 200 / AU

    #defining the time reference for each hour/day/etc the program updates parameters
    TIMESTEP = 3600*24 #1 day

    def __init__(self, x, y, radius, color, mass):
        #planets related configuration
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        #sun related configuration
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        #velocity inputs
        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, SUNMASS)
    sun.sun = True

    mercury = Planet(0.387 * Planet.AU, 0, 8, GREY, MERCMASS)

    venus = Planet(0.723 * Planet.AU, 0, 14, BEGE, VENUSMASS)

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, EARTHMASS)

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, MARSMASS)

    planets = [sun, mercury, venus, earth, mars]

    while run:
        clock.tick(60)
        #changing background color
        '''
        WIN.fill(COLOR)
        '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw(WIN)

        pygame.display.update()
    
    
    pygame.quit()

main()


#test