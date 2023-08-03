# Metaprograming 
# working with classes (types)
# working with functions (methods)

isinstance(3, int) # True
isinstance(3, object) # True
isinstance(3, str) # False
isinstance(int, type) # True
isinstance(3, type) # False
isinstance('hello', str) # True


issubclass(int, object) # True
issubclass(object, int) # False
issubclass(int, int ) # True
# issubclass(3, int ) # Error
issubclass(int , type) # False

issubclass(object, type) # False
# everything else is true

# everything in python is an object 
# classes of classes have speacial names - metaclass
# every object is an instance of a class


# type
# type(x) returns the type of x
# construct instance of type(name, bases, dict)

# example for type
def init_person(self, name) : self.name = name

def say_hi(self) : print(f"Hi, my name is {self.name}")

Person = type('Person', (), { '__init__' : init_person, 'say_hi' : say_hi,})

Person('George').say_hi()

# Inheritance of type
class metacls(type) :
    def __new__(cls, name, bases, dict) :
        dict['say_bye'] = lambda self : print('bye')
        return type.__new__(cls, name, bases, dict)
    

Person1 = metacls('Person', (), {
    '__init__': init_person,
    'say_hi': say_hi,
})

Person1('John').say_bye()

# # syntax sugar
# class Foo(A,B,C, metaclass = Bar) : 
#     x = 1
#     y = 2 

# Foo = Bar('Foo', (A,B,C), {'x' : 1, 'y' : 2})


# syntax sugar 2 : 
class Person(metaclass=metacls):
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print(f'Hi, My name is {self.name}')
Person('George').say_bye() # bye


# eval - evaluate an expression
# exec - evaluate a part of code
# compile
# we should not use them

from math import pi

def circle_area(r) :
    return pi * (r**2)
print(circle_area.__code__.co_code)

# import dis
# bite code
# instructions - kinda like assembler
import dis
dis.dis(circle_area.__code__.co_code)


# polish notation / prefix notation
# abstract syntax tree
# the body looks like this : 
# return
#   * 
#  / \
# /   \
#pi   **
#    /  \
#    r  2 
# prefix evaluateon
# its node-left-right traversal
# so basically depth first search
# we get return (* pi (r**2)) as we know from polish notation this is correct
 

# if we traverse it left-node-right 
# we will get the infix evaluation
# basically (return (*-pi (** r 2)))

# suffix - left-right-node
# we get ((pi (r 2 **) * ) return)


# bitecode
# ((pi (r 2 **) *) return) 
# pi r 2 ** * return 
# LOAD_GLOBAL 0 <=> pi
# LOAD_FAST 0 <=> r
# LOAD_CONST 1 <=> 2
# BINARY_POWER <=> **
# BINARY_MULTIPLY <=> *
# RETURN_VALUE <=> return 

# the module where we construct AST( abstract syntax tree ) code 
import ast
