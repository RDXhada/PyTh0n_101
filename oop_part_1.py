# absolutely everything is an object in python
# type(42) will return <class 'int'>
# type([]) will return as list class
# type(type) will return <class 'type'>

print(type(type))
print(type(24))
print(type(2.23))
print(type([]) is list) # should return true

# classed in Python
import math
class Vector : 
    def __init__(self, x, y, z) : 
        self.x = x 
        self.y = y 
        self.z = z 

    def coords(self) :
        return (self.x, self.y, self.z)
    
    def length(self) : 
        return math.sqrt(self.x**2 + self.y**2 + self.z)

# coords is a protected method
# we use self se we can access atributes

vec1 = Vector(1.0, 1.0, 3.5)
print(vec1.length())
print(vec1.coords())
print(Vector.length(vec1))

# classed are "open" by default
# methods that start with _ are protected [they can be used by the inherited classes]
# methods that start with __ are private [can only be used in the class, not on inherited classes]

# Mutable vs immutable
# most ojects in Python are mutable
# mutation method :
class Point :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    
    def length(self) : 
        return self.x + self.y
    
    def normalise(self) : 
        length = self.length()
        self.x /= length()
        self.y /= length()

# Non-mutating method
class Rectangle :
    def __init__(self, a,b) : 
        self.a = a
        self.b = b

    
    def perimeter(self) :
        return 2 * self.a + 2 * self.b

    def area(self) :
        return self.a * self.b
    
    def normalize(self) : 
        area  = self.area()
        self.a /= area
        self.b /= area

    def normalized(self) :
        return Rectangle(self.a / self.area(), self.b / self.area())
    
# similarity between objects
# we check if two objects have equal stuff with ==
# we can check if to names point to the same object with "is"
# we can define equality between objects from a given class with "eq"
# eq__ is implemented with "is"

class Vector1 :
    def __init__(self, a ,b, c) : 
        self._coords = (a,b, c)

    def __eq__(self, other) : 
        return self._coords == other._coords
    
# Dunder methods = double under methods
# predefine somekind of aspect of a behaviour of an object
# - add, substract, multiplu, truediv, floordiv, mod, and, xor, __or__ 
# and more arithmetic operators
# we can reshape standart types like ___int__, __float__, __complex__, __bool__

# objects that can be called as functions
class Stamp:
    def __init__(self, name):
        self.name = name
    def __call__(self, something):
        print("{0} was stamped by {1}" .format(something, self.name))

stamp = Stamp("The government")
stamp("That thing there")
    
# getattr and setattr
vec2 = Vector(1,2,3)
print(getattr(vec2, 'z'))
setattr(vec2, 'y', 55)
print(getattr(vec2, 'y'))

# static methods
class GoatSimulator : 
    goats = []
    @staticmethod
    def register(name) : 
        GoatSimulator.goats.append(name)
        print(len(GoatSimulator.goats), " goats are registered now")

    
GoatSimulator.register("Pip the Happy goat")
GoatSimulator.register("Peppa the non-binary goat")

# class methods
# we can used them so we can get the method of the class which has been called as a first argument 

class Countable :
    _count = 0
    def __init__(self, data) : 
        self.data = data
        type(self).increase_count

    @classmethod
    def increase_count(cls) : 
        cls._count += 1

    @classmethod
    def decrease_count(cls) :
        cls._count -= 1




# destructor
# we use __del__

class Car :
    _brand = ""
    _count = 0

    def __init__(self, data) :
        self.data = data
        type(self).increase_brand()


    @classmethod
    def increase_brand(cls) :
        cls._count+=1
        cls._brand += "{count}" 

    @classmethod 
    def decrease_brand(cls) :
        cls._count -= 1
        cls._brand += "{count}"

    def __del__(self) :
        type(self).decrease_brand()


#property methods 
# the decorator "@property" can be used so we can make a method pretend its a property

def adition(a,b) : 
        return Vector(a.x + b.x, a.y + b.y, a.z + b.z) 
import math 
class VectorTriple : 
    def __init__(self, x, y, z) :
        self.x = x
        self.y = y
        self.z = z 

    @property
    def length(self) : 
        return math.sqrt(self.x**2 + self.y**2)
    
    __add__ = adition
    
# property methods setters
class Color :
    def __init__(self, rgba) :
        self._rgba = tuple(rgba)

    @property
    def rgba(self) : 
        return self._rgba
    @rgba.setter
    def rgba(self, value) :
        self._rgba = tuple(value) 


print(VectorTriple(1.3, 2.2, 3.0) + VectorTriple(4.5, 5.5, 7.8))


