import math
import antigravity

class Point:

    def __init__(self, ix, iy):
        self.x = ix
        self.y = iy

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x = " + str(self.x) + ", y = " + str(self.y) + "."

    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)

    def reflectx(self):
        return Point(self.x * -1, self.y)

    def find_line(self, other):
        my = other.y - self.y
        mx = other.x - self.x

        slope = my / mx

        b = self.y - (slope * self.x)

        return "y = " + str(slope) + "x + " + str(b)

    def move(self, dx, dy):
        nx = self.x + dx
        ny = self.y + dy

        return Point(nx, ny)

    def distance(self, other):
        xdiff = self.x - other.x
        ydiff = self.y - other.y

        dist = math.sqrt(xdiff ** 2 + ydiff ** 2)
        return dist

    def find_circle(self, x2, y2, x3, y3):
        x1 = int(self.x)
        y1 = int(self.y)

        X = ((x1**2 + y1**2)*(y2-y3) + (x2**2 + y2**2)*(y3-y1) + (x3**2 + y3**2)*(y1-y2))/2*(x1*(y2-y3) - y1*(x2-x3) + x2 * y3 - x3 * y2)
        Y = ((x1**2 + y1**2)*(x3 - x2) + (x2**2 + y2**2)*(x1 - x3) + (x3**2 + y3**2)*(x2 - x1))/2*(x1*(y2-y3) - y1*(x2-x3) + x2 * y3 - x3 * y2)
        R = math.sqrt((X - x1)**2 + (Y - y1)**2)

        A = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * x3 - x3 * y2
        B = (x1 ** 2 + y1 ** 2) * (y3 - y2) + (x2**2 + y2 ** 2) * (y1 - y3) + (x3 ** 2 + y3**2) * (y2 - y1)
        C = (x1 ** 2 + y1 ** 2) * (x2 - x3) + (x2**2 + y2 ** 2) * (x3 - x1) + (x3 ** 2 + y3**2) * (x1 - x2)
        D = (x1 ** 2 + y1 ** 2) * (x3 * x2 - x2 * x3) + (x2**2 + y2 ** 2) * (x1 * y3 - x3 * y1) + (x3 ** 2 + y3**2) * (x2 * y1 - x1 * y2)

        return (A, B, C, D)

j = Point(-3, 4)
k = Point(4, 5)
l = Point(1, -4)

#print(j.distanceFromOrigin())

#print(j.distance(k))

#print(j.halfway(k))

#print(j.reflectx())

#print(j.find_line(k))

#print(j, k)

#print(j.move(3, -5))

print(j.find_circle(k.getX(), k.getY(), l.getX(), l.getY()))
