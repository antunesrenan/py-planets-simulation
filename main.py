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
        
        if len(self.orbit) >= 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))
            #draw orbital lines
            pygame.draw.lines(win, self.color, False, updated_points, 2)
        
        #draw planets
        pygame.draw.circle(win, self.color, (x, y), self.radius)

    #defining the distance between objects
    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        
        #defining if other object is "Sun", if it is we keep value for distance
        if other.sun:
            self.distance_to_sun = distance

        #defining the force of attraction (Newton's law of universal gravitation)
        force = self.G * self.mass * other.mass / distance**2
        
        #defining angle using Python library Math to simulate orbit
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        #Using Newton's Second Law (F=m*a) to add velocity and update frame
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, SUNMASS)
    sun.sun = True

    mercury = Planet(0.387 * Planet.AU, 0, 8, GREY, MERCMASS)
    mercury.y_vel = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 14, BEGE, VENUSMASS)
    venus.y_vel = -35.02 * 1000

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, EARTHMASS)
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, MARSMASS)
    mars.y_vel = 24.077 * 1000

    planets = [sun, mercury, venus, earth, mars]

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))

        #changing background color
        '''
        WIN.fill(COLOR)
        '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()
    
    
    pygame.quit()

main()