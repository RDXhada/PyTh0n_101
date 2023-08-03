print(__name__)
# everything in python is part of a module
# every file is a module (the name of the file)


# import
# every module is imported only once
#import iterators_generators # we can import a file
print("Hey, how you doing") # every import is output from the file

import unittest
print(unittest.__name__)


from random import shuffle
import itertools as it
print(it.__name__)


# fro the imports we can import specific modules that we only need
# from module import what_i_need, and_this_other_thing

import itertools
print(dir(itertools))

from itertools import permutations


# search order
import sys
print(">> Shows the system file path:\n", sys.path)

# we can use :
# from . import index
# from .. import whatever
# from ..child import twins

#.pyc files
# precompiles .py files
# python optimisation
# in python 3 thay sit in the __pycache__ directory
# we can deactivate them (generally)
# we dont think about them, except for version control


# import pdb
print("Debugging with something better than print")
import pdb; pdb.set_trace() # debugging 

# what can be overall a module in python
# a file with .py 
# directory that has file with __init__.py

