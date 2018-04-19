import random
print(random.randrange.__doc__)

"""projectile.py
Provides a simple class for modeling the flight of projectiles."""

from math import pi, sin, cos

class Projectile:
    """Simulates the flight of simple projectiles near the earth’s
    surface, ignoring wind resistance. Tracking is done in two
    dimensions, height (y) and distance (x)."""
    def __init__(self, angle, velocity, height):
        """Create a projectile with given launch angle, initial
        velocity and height."""
        self.xpos = 0.0
        self.ypos = float(height)
        theta = pi * float(angle) / 180.0
        self.xvel = float(velocity) * cos(theta)
        self.yvel = float(velocity) * sin(theta)

    def update(self, time):
        """Update the state of this projectile to move it time seconds
        farther into its flight"""
        self.xpos = self.xpos + float(time) * self.xvel
        yvel1 = self.yvel - 9.8 * float(time)
        self.ypos = self.ypos + float(time) * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

    def getY(self):
        "Returns the y position (height) of this projectile."
        return self.ypos

    def getX(self):
        "Returns the x position (distance) of this projectile."
        return self.xpos
