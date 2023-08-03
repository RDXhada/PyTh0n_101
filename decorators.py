# to understand decorators we need to understand - methods, functions, nested functions,
# scope, closures


a = 2
v = 10

global_one = 1
def foo():
    local_one = 2
    print("Locals are",locals()) # returns a dictionary of all local stuff used 

foo()
print("Globals are: ", globals()) # returns a dictionary of all global stuff used

# Nested functions
def outer(x) :
    print(x) 
    def inner() :
        x = 0
        print(x)
    inner()
    print(x)

# name inner goes to locals() of the outer
# keyword nonlocal lets us redefine a name, defining a scope
# functions are first-class objects 
# we can return functions as a result
# we can write/save them in collections
# they have id()

# Closures - when a nested function are accessed by a variable, defined by the scope of the function
# example
def start(x) :
    def increment(y) :
        return x + 2*y
    return increment

first_increment = start(0) # first define what is x, in our case 0
second_increment = start(8) # x is 8

print(first_increment(1)) # y = 1, so 0 + 2*1 = 2
print(second_increment(3)) # y is 3, si 8 + 2*3 = 14

print(first_increment(2)) # y is 2, so 0 + 2*2 = 4

# one more problem so we can understand decorators better
def spam(n):
    spams = ("spam", ) * (n - 1)
    return "I would like {} and spam".format(", ".join(spams))
def eggs(n):
    return "I would like {} eggs".format(n)

print(spam(3))
print(eggs(2))


def served_by(func, server):
    def cached_server(n) : 
        return "{}, dear {}".format(func(n), server)
    return cached_server

eggs = served_by(eggs, "sir")
print(eggs(2))
spam = served_by(spam, "madam")
print(spam(4))

def thank_you(func) :
    def with_thanks(n) : 
        return "{}. Thank you very much!".format(func(n))
    return with_thanks

eggs = thank_you(served_by(eggs, "madam"))
print(eggs(3))

# fibonacci example
#memoize
def memoize(func): 
    memory = {}
    def memoized(*args): 
        if args in memory:
            return memory[args]
        result = func(*args) 
        memory[args] = result 
        return result
    return memoized


@memoize
def fibonacci(n) :
    if n in [0, 1]:
        return 1 
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))

# other example for decorator
def notifyme(f):
    def logged(*args, **kwargs):
        print(f.__name__, ' called with', args, 'and', kwargs)
        return f(*args, **kwargs) 
    return logged

@notifyme
def square(x) : 
    return x * x
result = square(25)


# eggs, spam and server
# but better done with decorators
 
def servedby(server) :
    def decorator(func) :
        def cached_server(n) :
            return "{}, dear {}".format(func(n), server)
        return cached_server
    return decorator

def thankYou(func) : 
    def withThanks(n) : 
        return "{}. Thank you very much!".format(func(n))
    return withThanks

@servedby("madam")
def spam1(n) : 
    spams = ("spam", ) * (n - 1)
    return "I would like {} and spam".format(", ".join(spams))

@thankYou
@servedby("madam")
def eggs1(n) :
    if n == 12 : 
        return "I would like a dozen eggs"
    return "I would like {} eggs".format(n) 
    

print(spam1(5))
print(eggs1(12))

#wrapper functions
def func1(func) :
    def wrapper(*args, **kwargs) : 
        print('Start')
        val = func(*args, **kwargs) 
        print('End')
        return val

    return wrapper
@func1 # decorator
def f(a) : 
    print(a)

# x = func1(f)
# x() # function aliasing

f('Hey yo')

def add(x,y) :
    return x + y


print(add(10,20))

# timer decorators
import time
def timer(func) : 
    def wrapper() :
        before = time.time()
        func()
        print(f"Function took {time.time() - before} seconds")

    return wrapper

@timer
def run_time() : 
    time.sleep(5)

@timer
def run_time2() : 
    time.sleep(0.14)

run_time()
run_time2()

# good for checking algorythms runtime and stuff