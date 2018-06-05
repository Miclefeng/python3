# area.py 
import math

def area(radius):
    """ Returns the area of a circle with the given radius.
    For example:
    area(5.5)
    95.033177771091246
    """
    return math.pi*radius**2

print(area(1))
print(area(5.5))
print(2*(area(3)+area(4)))
print(area.__doc__)

