from points import Point
import math

class Circle:

    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError("promien ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):       # "Circle(x, y, radius)"
        return ("Circle("+ str(self.pt.x) + ", " + str(self.pt.y) + ", " + str(self.radius) + ")")

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):           # pole powierzchni
        return (math.pi * self.radius * self.radius)

    def move(self, x, y):     # przesuniecie o (x, y)
        self.pt.x += x
        self.pt.y += y

    def cover(self, other):   # okrag pokrywajacy oba
        odlSrodk = math.sqrt(math.pow(other.pt.x - self.pt.x, 2) + math.pow(other.pt.y - self.pt.y, 2))
        if odlSrodk <= math.fabs(self.radius - other.radius): #jeden w drugim
            if self.radius > other.radius:
                return self
            return other
        else:
            tmpX = (self.pt.x + other.pt.x)/2. #wyznaczam sdodek na prostej laczacej srodki okregow
            tmpY = (self.pt.y + other.pt.y)/2.
            tmp = math.sqrt(math.pow(other.pt.x - self.pt.x, 2) + math.pow(other.pt.y - self.pt.y, 2)) #dlugosc odcinka laczacego srodki
            tmpR = 0
            if self.radius > other.radius:
                tmpR = self.radius + (tmp/2.) #promien okregu
            else:
                tmpR = other.radius + (tmp/2.)
            return Circle(tmpX, tmpY, tmpR)
