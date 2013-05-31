import math

class Circle:
    '''2D Circle object'''
    def __init__(self,radius):
        '''initialiser for instance of circle'''
        self.__radius = radius

    def get_radius(self):
        '''accessor for radius of circle'''
        return self.__radius

    def calc_area(self):
        '''calculate area of circle'''
        return self.__radius ** 2 * math.pi

    def calc_circumference(self):
        '''calculate circumference of circle'''
        return self.__radius * 2 * math.pi


c = Circle(5)
print('Radius:', c.get_radius())
print('Area:', c.calc_area())
print('Circumference:', c.calc_circumference())
