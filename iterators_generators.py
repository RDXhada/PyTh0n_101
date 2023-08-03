# iterables - list, set, dict, tuple, map and filter
# everything in collections library
# __getitem__ objects
# iterable has  __iter__ method
# iterator has __next__ method

# we can output numerous times with lists, sets, dicts and etc.
# example
squares = map(lambda x : x ** 2, range(5))
for number in squares :
    print(number)

for number in squares : 
    print(number)

# example for lazy - lazy iterables just iterate once
# we generate the elemets when they are needed
squares1 = map(lambda x : x ** 2 , range(5))
print(list(squares1))

# iter example 1
nikulden = ['riba', 'bira', 'karofi']
nikulden_iterator = iter(nikulden)
print(next(nikulden_iterator))
print(next(nikulden_iterator))

# iter example 2
class SequenceIterable() :
    def __iter__(self) :
        return SequenceIterator()
    
class SequenceIterator :
    def __init__(self) :
        self.num = 0

    def __next__(self) :
        value = self.num
        self.num += 3
        if value > 15 :
            raise StopIteration
        return value
    
# iter example 3
class Sequence :
    def __init__(self) :
        self.num = 0
    def __iter__(self) : 
        return self 
    def __next__(self) :
        value = self.num
        self.num += 3
        if value > 15 :
            raise StopIteration
        return value
    
# Iter 2.0 example
class AddTwo : 
    def __init__(self) :
        self.start = 0
    def __iter__(self) :
        return self 
    def __next__(self) :
        self.start += 2
        return self.start
    
    __call__ = __next__


my_iter = iter(AddTwo(), 10)
print(list(my_iter))


# iterators are lazy!

# difference between sort/sorted
# sort sorts the original array
# sorted returns a new sorted array

# difference betwen revese/rebersed
# reversed returns an iterator

# example
numbers  = [122,3,4,5,-7,2]

print(list(reversed(numbers)))


# generators
# they do not store the values in the memory, but generated whenever is needed
# instead of return we use 'yield'


# example
class SquareUpTo :
    def __init__(self, up_to) :
        self.up_to = up_to
        self.num = 0


    def __iter__(self) :
        return self
    
    def __next__(self) : 
        if self.num > self.up_to :
            raise StopIteration 
        
        square = self.num ** 2
        self.num += 1
        return square
    

def squares_up_to(number) :
    value = 0
    while value <= number :
        yield value **2
        value += 1


# list/set/dict comprehension
print([x ** 2 for x in range(5) if x % 2 == 0])
print({x + 1 : x ** 2 for x in range (5) if x % 2 == 0})
print({x ** 2 for x in range (5) if x % 2 == 0})

# generator expression
example_generator = (letter * 5 for letter in "Classy")
print(list(example_generator))

# map and filter
# they accept iterables and return iterators
def numbers1() :
    num = 0
    while True :
        yield num 
        num += 1

doubles = map(lambda num : num * 2, numbers1())

# enumerate
necesities = ['beer', 'fish', 'nikolay']
for index, necesity in enumerate(necesities, 1) :
    print (f"{index} - {necesity}")


# zip
from itertools import zip_longest
numbers =  [1,2,3,4,45]
letters = ['a', 'b', 'c', 'd', 'e']
longest = range(5)
zipped_normal = zip(numbers, letters, longest)
zipped_longest = zip_longest(numbers, letters, longest, fillvalue='?')
print(list(zipped_normal))
print(list(zipped_longest))

# itertools - lazy methods/functions that can be used when working with iterable objects

from itertools import accumulate
sums = accumulate(range(1, 101), lambda a, b : a + b)
# print(list(sums))
print(next(sums))

# itertools combinations
from itertools import combinations
example = [1,23,4,8]
combinations_of_two = combinations(example , 2)
print(list(combinations_of_two))
print(list(combinations_of_two))


# itertools cycle
from itertools import cycle
# x = cycle([1,2,3])
# for i in x :
#     print(i) 
# will result in endless output

# itertools count
from itertools import count
i = iter(count(5,3))
print(next(i))
print(next(i))

# iteratools repeat
from itertools import repeat
print(list(repeat(10, 10))) # repeat 10, 10-times


# more iteratools - chain, compress, dropwhile, iteratefalse, product, permutation