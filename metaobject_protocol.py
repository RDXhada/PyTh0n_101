# questionaire

import re
sentence = 'we are humans'

matched = re.match(r'(.*) (.*?) (.*)', sentence)
print(matched.groups())

# atributes 
foo = []
print(dir(foo))

# meta - self referring
# meta programming - programs that are made to make programs
# macros in metaprogramming
#define X = 42
#int x = X
# templates
# reflection
# list and other - the code and data share similar format
def fma(a,x,y=0) :
    return a*x + y
# other eay
def fma1(a,x,y=0) :
    return a.__mul__(x).__add__(y)
print(fma(2,3,4))
print(fma1(2,3,4))

print(dir(fma))

# descriptors
class B :
    def __get__(self, instance, owner) :
        return "You came in the wrong neighborhood"
    
    def __set__(self, instance, value) : 
        return print("You think you can change my personality?")
    
    def __delete(self, instance) :
        print("Cant touch this tu dum")

class A :
    foo = B()

a = A()
a.foo
a.foo = 'bravo'
# del a.foo # this will result in error


# bound methods
increment = (1).__add__
example_ex = map(increment, [0,1,2,3])
print(list(example_ex))

# bound methods
class MyMethod :
    def __init__(self, func) :
        self.func = func
    
    def __get__(self, instance, owner) :
        if instance :
            return lambda : self.func(instance)
        else :
            return lambda explicit_instance : self.func(explicit_instance)
        
class Python : 
    name = 'Monty'
    greet = MyMethod(lambda self : f"My name issss {self.name}")


snake = Python()
print(snake.greet())
snake.name = "Sharo"
# Python.greet() will result in error
print(Python.greet(snake))

# casts ;
# __bool__(self) , __float__(self), __int__(self), __str__(self)
# representations :
# __rept__(self), __str__(self), __doc__, __dir__(self)

# Arithmetics
# in Python 3 they are a little different (for compatbility reasons)
# __add__(self, a) 
# __radd__(self, a)
# __sub__(self, a)
# __rsub__(self, a)
# __div__(self, a) 
# __rdiv__(self, a) -> __rtruediv__(self, a)
# __floordiv__(self,a)
# __rfloordiv__(self,a)
# __truediv__(self, a)
# __rtruediv__(self,a)
# __divmod__(self, a)
# __rdivmod__(self, a)

# NotImplemented, Elipsis

# __abs__(self), __pos__(self), __neg__(self)


# Binary/bit arithmetics
# __and__(self, a)
# __or__(self, a)
# __xor__(self, a)
# __rshift__self, n)
# __lshift__(self, a)

class CustomNumber:
    def __init__(self, value):
        self.value = value

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return other / self.value
        else:
            raise TypeError("Division is only supported with numeric types.")

num1 = CustomNumber(10)
result = 20 / num1
print(result)  # Output: 2.0

# hashing and equality
# __hash__(self)
# __eq__(self, a)
# __ne__(self, a)

# comparisons
# __lt__(self, a)
# __le__(self, a)
# __gt__(self, a)
# __ge__(self, a)

# with
# __enter__
# __exit__


# Atrributes
# __getattribute__(self, name)
# __getattr__(self, name)
# __setattr__(self, name, value)
# __delattr__(self, name)
# __dir__(self)


# Iterators
# __iter__(self)
# __next__(self)

# Collections - len, contains, getitem, setitem, delitem

# Metaatributes
# __dict__
# __slots__
# __class__
# __globals__
# __name__


# functions 
# __code__
# __call__(self, *args, **kwargs)


# contructing obj
# __new__(cls, *args, **kwargs)
# __init__(self, *arhs, **kwargs)

# __new__ is the real constructor of obj
# __init__ is only the initializer

class Vector(tuple) :
    def __new__(klass, x, y) :
        return tuple.__new__(klass, (x,y))
    
    def __add__(self, other) :
        if not isinstance(other, Vector) : 
            return NotImplemented 
        return Vector(self[0] + other[0], self[1] + other[1])
    
class A(int) : pass
class B :  pass
class C(A,B, int) :  pass
print(C.mro()) # or C.__mro__