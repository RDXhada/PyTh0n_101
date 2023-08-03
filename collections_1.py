# types in Python
# int , float, complex(number), string, bool, None
# collections - list, tuple, dictionary, set
# control structures - while, for, (break, continue), switch - match/case
# 4 interval identation with : for start of block
# functions can be called in other functions 
# All collections are iterable
good_food = ['coffe', 'cheese', 'tomatoes', 'spaghetti']
for food in good_food:
    print(f"I tend to like {food}")

print(good_food[1])
# reversed
print(good_food[-1])

# Lists - списъци
wild_animals = ["Orangutan", "Fox", "Aligator", "Cheetah", "Tiger", "Wolf", "Volibear(LoL :D)"]
print(wild_animals[0 : 3])
print(wild_animals[-1])
print(wild_animals[-3 : 0 : -1])


# lists consists of references to the elements
coffe, cheese, tomatoes, spaghetti = 'coffe', 'cheese', 'tomatoes', 'spaghetti'
things_i_like_a_lot = [spaghetti, tomatoes]
if things_i_like_a_lot[1] == tomatoes:
    print(f"I like {tomatoes} because of the umami!")
else :
    print(f"I like {spaghetti} because its italian ;0")

things_you_like = [cheese, coffe, tomatoes]
print(things_i_like_a_lot[0] == things_you_like[1]) #False
# same thing is
print(things_i_like_a_lot[1] is things_you_like[2]) # True


types_of_wines = ['chardonnay', 'merlot', 'white', 'rose', 'sauvignon blanc']
types_of_wines.append(types_of_wines) # type: ignore
print(types_of_wines[-1] is types_of_wines) # should return true
print(types_of_wines[-1])
print(types_of_wines[0])

teas = ['chai', 'earl grey', 'jasmine', 'oolong']
good_dinner = [good_food, types_of_wines]
print(good_dinner[0][3])

good_dinner[0][1] = ['wasagna', 'pizza', 'steaks'] # type: ignore
print(good_food)
# print(good_dinner)


# list methods
# .index(element)
# .count(element) - number of occurences of the specific element
# .append(element)\
# .extend(elements) - adds elements from another list (like a +)
# .sort - sorts the list
# ..there is more - can check the library/class
somekind_of_list = [1,223,5,5]
somekind_of_list.extend([4,5,87])
somekind_of_list.sort()
print(somekind_of_list)

# Range
nums = range(3)
for n in nums :
    print("We can count to", str(n))
    #print("..." + str(n)) is an option too


# Tuple
humans = ('Rick', 'Morty', 'Koleto')
# humans = 'Rick',
# humans = ('Rick')
# methods .index and .count
print(humans)

(i, j) = (69,102)
print(i)
# brackets can be avoided, though crucial for readability

(q, *w, e) = 1,2,3,4,5
print(*w)
# q = 1
# w = 2,3,4
# e = 5

print((1,2)<(1,3)) # type: ignore
print((1,2)<(1,2,3)) #подмножество

# print((1,2) < [1,3]) this will result in error

# Queue, fifo buffer, list - populat data structures
adjectives = []
def add_adjectives(items) :
    adjectives.append(items)


def get_adjective():
    return adjectives.pop(0)

add_adjectives('Hello')
add_adjectives('World')
print(' '.join(adjectives))


# Sets
favourite_numbers = set()
favourite_numbers.add(5)
favourite_numbers.add(7)
favourite_numbers.add(69)
favourite_numbers.add(102)
print(favourite_numbers)

for fav in favourite_numbers :
    print(f"I really like the number {fav}") 
    # other option is "I really like" + str(fav)

# set operations
print({1,2,3} | {2,3,4})
print({1,2,3} & {2,3,4})
print({1,2,3} - {2,3,4})
print({1,2,3} ^ {2,3,4}) # believe this is xor 
print({2,3} < {1,2,3}) # подмножество
print({2,3} == {2.0, 3, 4}) # false

# {} is not an empty set!

# Dictionary
artist_names = {'Justin' : 'Bieber', 'Conor' : 'Maynard', 'Lil' : 'Wayne'}
print('Conor\'s last name is ' + artist_names['Conor'])
# {} is an empty dictionary!


artist_names['Mary'] = 'Jane'
print(artist_names)

# different ways to create a dictionary
dict(France = 'Paris', Bulgaria = 'Sofia')

# list of doubles
dict([('One', 'I'), ('Two', 'II'), ('Ten', 'X')])

# list of keys and values as default values
lmao = dict.fromkeys([1,2,3,28,5], 'Unknown')
print(lmao)

name_data = [('John', 'Tilsit'), ('Eric', 'Cheshire'), ('Michael', 'Camembert'), ('Terry', 'Gouda'), ('Terry', 'Port Salut'), ('Michael', 'Edam'), ('Eric', 'Ilchester'), ('John', 'Fynbo')]

# dictionary function and how to work with it
def cheeses_by_owner(cheese_data) :
    by_owner = {}
    for owner, cheese in cheese_data : 
        if owner in by_owner:
            by_owner[owner].append(cheese)
        else:
            by_owner[owner] = cheese
    return by_owner

# example exercise
# [Jane, Jane, Marko, Jane] should become [Jane, Jane1, Marko, Jane2]
def add_numbers_to_duplicate_names(names):
    name_count = {}
    result = []
    for name in names:
        if name in name_count:
            name_count[name] += 1
            name_with_number = f"{name}{name_count[name]-1}"
            result.append(name_with_number)
        else:
            name_count[name] = 1
            result.append(name)
    return result

print(add_numbers_to_duplicate_names(['Jane', 'Jane', 'Marko', 'Jane']))


# different types of collections - deque, orderedDict, defaultDict, Counter, namedtuple

# Deque (commands : append(), appendleft(), clear(), copy(), count(), extend(), extendLeft(), index[x[, start[, stop]]], insert(), pop(), popLeft(), remove(), reverse(), rotate(), maxlen())

from collections import deque
d = deque('water')
for elem in d :
    print(elem.upper())


d.append('melon')
d.appendleft('LOL')
d.pop()
d.popleft()
print(list(d))
print(d[0]) # peek leftmost item
print(d[-1]) # peek rightmost item
print(list(reversed(d))) # print elements in reversed manner 
print('w' in d) # should return true
d.extend('melon') # add multiple elements at once
print(list(d))
d.rotate(-1) # rotate left
d.rotate(1) # rotate right

e = deque(reversed(d)) # make a new deque - reversed version of d
d.clear()
# d.pop() # cannot pop from empty deque
print("New reversed deque : ", list(e))
d.extendleft('abc')  # extendleft() reverses the input order
print("Updated old deque but with reversed inputed elements : ", list(d))


# Ordered dictionary  - popitem(last = True) [LIFO METHOD] 
# move_to_end(key, last = True)
from collections import OrderedDict
ord_dict = OrderedDict().fromkeys('abcde')
ord_dict.move_to_end('b') # move the element to either of the two ends of the Ordered dictionary
print(''.join(ord_dict))
ord_dict.move_to_end('b', last = False)
print(''.join(ord_dict))


#Default dictionary
# list
from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k,v in s:
    d[k].append(v)

print(sorted(d.items()))

s = 'missisipi'
d = defaultdict(int)
for k in s :
    d[k] += 1

print(sorted(d.items()))

def constant_factory(value) :
    return lambda : value
d = defaultdict(constant_factory('<default_place>'))

d.update(name = 'John', action = 'ran')
print('%(name)s %(action)s to %(object)s' % d)


# Counter 
from collections import Counter
# a counter tool is used to support convenient and rapid tallies
count = Counter()
for word in ['red', 'blue', 'yellow'] :
    count[word] += 1
print(count)

# find the ten most common words in hamlet 
# import re 
# words = re.findall(r'\w+', open('1000-stdout.txt').read().lower())
# print(Counter(words).most_common(5))
# file direcitory must be imported correctly in open() method

c = Counter() # empty counter
c = Counter('lmao') # a new counter from an iterable
c = Counter({'red' : 4, 'blue' : 14}) # a new counter from mapping
c = Counter(cats = 4, dogs = 5) # a new counter form keyword arguments

c = Counter(['eggs', 'bread', 'cheese']) 
print(c['bacon']) # returns 0 because its a missing element
# setting the count to zero does not remove an elements from a counter
# we use del c[] instead
c['milk'] = 0 # counter entry with zero count
del c['milk'] # del actually removes the entry

# different methods for Counter - elements(), most_common([n]) - most common elements and their count
# subtract[iterable/mapping] - elements are subtracted from an iterable or from another mapping (or counter),
# its like dict.udpate() but subtracts counts instead of replacing them
# total() - sum of the counts
# fromkeys(iterable)
# update([iterable/mapping])

print("Total of all counts of Counter c",c.total())
c.clear() # reset
list(c) # list unique elements
set(c) #convert to a set
dict(c) # convert to a dictionary
c.items() # convert TO a list of (element, counter) pairs
Counter(dict(c)) # convert FROM a list of (element, counter) pairs
c.most_common()[:-15-1:-1] # n least common elements in our case 15
c['milk'] = 1
print(+c) # remove zero and negative counts

c = Counter(a = 3, b = 1)
d = Counter(a = 1, b = 2)
print(c + d)
print(c - d)
print(c & d) # intersection
print(c | d) # union
print(c == d) # c[x] == d[x]
print(c <= d) # c[x] <= d[x]

# unary addition and substractions for Counter are shortcuts for adding an empty
# counter or substraction from an empty counter
c = Counter(a = 8 , b = -12)
print(+c)
print(-c)
# NB :  Counters were primarily designed to work with positive integers to represent running counts; 


# Named tuple
from collections import namedtuple
#example
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y = 22)
print('Tuple result', p[0] + p[1])
x, y = p
print(x,y)

# Named tuples are especially useful for assigning field names to result tuples returned by the csv or sqlite3 modules

# _make(iterable) - makes a new instance from an existing sequence/iterable
t = [789,339]
print(Point._make(t))

# _asdict() - return a new dictionary which maps field names to the values
p = Point(x = 11, y = 22)
print(p._asdict())

# _replace(**kwargs) - return a new instance of the named tuple replacing specified fields 
# with their values
print(p._replace(x = 333, y = 69))

# _fields() - tuple of strings listing the field names 
print(p._fields)

# _field_defaults() - dictionary mapping field names to default values
Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
print(Account._field_defaults)

# getattr() - retrieve field whose name is stored as a string
print(getattr(p , 'y'))

# NB : To convert a dictionary to a named tuple, use the double-star-operator 
