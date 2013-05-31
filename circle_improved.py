import math
from random import random, seed

class Circle(object):
    '''2D Circle object'''

    __slots__ = ['diameter']
    version = '0.7'
    
    def __init__(self,radius):
        '''initialiser for instance of circle'''
        self.radius = radius

    def area(self):
        '''calculate area of circle from perimeter'''
        p = self.__perimeter()
        r = p / math.pi / 2.0
        return r ** 2 * math.pi

    def perimeter(self):
        '''calculate perimeter of circle'''
        return self.radius * 2 * math.pi

    __perimeter = perimeter

    @property
    def radius(self):
        '''Radius of a circle'''
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    @classmethod
    def from_bbd(cls, bbd):
        '''Construct a circle from a bounding box diagonal'''
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    @staticmethod
    def angle_to_grade(angle):
        '''Convert angle in degree to a percentage grade'''
        return math.tan(math.radians(angle)) * 100.0

#basic usage
print('Using Circle version', Circle.version)
c = Circle(5)
print('Radius:', c.radius)
print('Area:', c.area())
print('Circumference:', c.perimeter())
print()

#average area of random circles
seed(8675309)
n = 100000
circles = [Circle(random()) for i in range(n)]
print('The average area of', n, 'random circles')
avg = sum([c.area() for c in circles]) / n
print('is {0:.3f}'.format(avg))
print()

#Rubber sheet company
cuts = [0.1, 0.7, 0.8]
circles = [Circle(r) for r in cuts]
for c in circles:
    print('A circlet with a radius of', c.radius)
    print('has a perimeter of', c.perimeter())
    print('and a cold area of', c.area())
    c.radius *= 1.1
    print('and a warm area of', c.area())
    print()

#National Tire chain
class Tire(Circle):
    '''Tires are circles with a corrected permieter'''

    def perimeter(self):
        '''Circumference corrected for the rubber'''
        return Circle.perimeter(self) * 1.25

t = Tire(22)
print('A tire of radius', t.radius)
print('has an inner area of', t.area())
print('and an odometer corrected perimeter of')
print(t.perimeter())
print()

#National graphics company
c = Circle.from_bbd(25.1)
print('A circle with a bbd of 25.1')
print('has a radius of', c.radius)
print('and an area of', c.area())
print()
