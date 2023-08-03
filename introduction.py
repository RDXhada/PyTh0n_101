#Introduction to Python(just for syntax learning exercise)
print(59 + 30)
a = 6 ** 8
b = a
print("This is b from a:",b)
a = 20
print("This is b when I change a:", b)
print("This is the changed a:", a)
text = "hello world"
print(text)
print("Floating point sum", 0.3 + 0.35)
print("Floating point deletion", 12/13)

capsLockedText = "wow bruh".upper()
print(capsLockedText)
print(2j * 3j)
print("Hello\nlmao")
print("HELL"[1])

# function returning none
def noneFunction():
    return None

print(noneFunction)
# types of whatever 
print(type(5.5))
# we can do type(type) as well [even nested ones like type(type(type)) and etc.]

# data structures - list,dictionary,tuple,set!
#lists
my_list = []
#more options for declarations of list is : 
my_list1 = list()
# appending elements
my_list.append(35)
my_list.append(21)
my_list.append("wowza")
my_list[0] = 2023
my_list.append((12,3)) # we can append tuples as well - pretty neat
print(my_list)

# things to note - lists are mutable
# lists have a non fixed length 
# fast for index search, slow for value search
# guaranteed order
# elements can be of different types - thus lists are heterogenic

print(my_list[1] == 21)

my_other_list = ['foo', 'bar', 'quix', 'tata', 'santa']
print(len(my_other_list))
del my_other_list[1]
print(my_other_list)
print('tata' in  my_other_list) 
# print(False in my_other_list)

# Dictionary
ages = {'Leon' : 25, 'Kiril' : 45}
ages['Mario'] = 21
ages['Jackie'] = 18
print(ages.get('Kiril'))
print(ages.get('Peepo', 'no such person'))

# note for dictionaries - order is not guaranteed!
# we have a key and a value 
# dictionary = hashable = associative array

# tuple, n-ary, courtege
args = (2.2,3.5,8,112)
print(args[3])
# this will result in error - it is immutable
# args[2] = 9.9
# print(args[2])
# tuple order is guaranteed 
# brackets can be avoided, though for readability they are crucial


# set
unique_numbers = {2,3,5,6,5,7,10}
print(unique_numbers)
unique_numbers.add(12)
unique_numbers.remove(3)
print('After changes :', unique_numbers)
# a set is a collection of non repeating number - thus unique numbers
# order is not guaranteed 
# we dont have direct access to a specific element, saldy
# we can check for references

# Mutability vs immutability
a1 = 3
a1 += 2
#a now refers to 5
#rather than changing the 3 to a 5, a now refers "->" to an other value (5 for our example)
b1 = [23,4,67,7,7]
b1.append(55)
# b1 becomes 23,4,67,7,7,55
# this code changes the list which refers to b1, thus making lists mutable
# for a key value on a dict or element on a set we can only use immutable values


#if, else if, else
conditionNumber = 3
if conditionNumber == 3:
    print("Number is 3!")
elif conditionNumber == 3 and not b == 22:
    print("Number is 3, but b is not 22!")
else:
    print("Number is something else or b is 22!")

# we dont need brackets in the conditions
# we use and, or, not instead of &&, ||, !
# False can be : False, None, 0, 0.0, 0j, empty array, empty tuple/lis/dictionary/set/frozenset


findListNumber = 2023
if findListNumber in my_list: 
    print(findListNumber, "is in my_list!")
else: 
    print(findListNumber ,"is not in my_list!")

#every block of code starts from ":" and ends when we go back to the previous identation

# While
loopNumber = 10
while loopNumber < 20:
    loopNumber += 1
    print(f"Looping {loopNumber}")


# For
evenNumbers = [2,4,8,16,32,64]
for e in evenNumbers:
    print(f"{e} squared is:",e ** 2)

people = {"Bobby" : 33, "Pedro" : 17, "Denislav" : 6, "Renee" : 19}
for name, age in people.items():
    print("{} is {} years old".format(name, age))


# lets to the same loops but in C-like manner
for i in range(73, 2040):
    if i % 3 == 0 and i%2 == 0 and i % 73 == 0:
        print(i)

# every N-th number
for j in range(0,101,10):
    print(j)

# reversed 
for k in range(100, 0, -10):
    print(k)


# break and continue work the same for every language
# swift case - no such thing, but after python 3.10 
# there is a match/case
# example for switch case in python (>3.10)

http_status = 401
match http_status:
    case 400: 
        print("Bad request!")
    case 401:
        print("Authentication error")
    case 404:
        print("Not found!")



# Functions 
def helloWorld(your_planet, my_planet):
    return f"You are from {your_planet}, and I am from {my_planet}!"

print(helloWorld("Mars", "Earth"))

def multiplication(a,b,c):
    return a*b*c

print(multiplication(1,2,3))

def isAPythagoreanTriangle(a,b,c):
    if a * a + b * b == c * c :
        return True
    else :
        return False

print(isAPythagoreanTriangle(3,4,5))
print(isAPythagoreanTriangle(3,2,3))


# variable number of arguments
def variableFunction(first, *args, **kwargs):
    return first, args, kwargs


print(variableFunction('hello there', 1,2,3,4, name='Kiril', age=23))
# functions can take a variable number of arguments 
# args is a tuple
# kwargs is a dictionary


#functions are object!
def dog():
    print("Woof")

def call(function, times):
    for _ in range(times):
        function()

print(call(dog, 4))