# marshalling to Python (converting strings and ints from C to Python)
# marshalling from C to Python
from ctypes import *
# libc = cdll.LoadLibrary('/Users/dzhemshenolov/Documents/CraftDemoTask/Quickbase learning /python stuff /oop_part_1.py')
# print(libc.time(None))
# libc.printf(b'good morning world')
i = c_int(66)
print(i, i.value)
i.value = -999
print(i, i.value)

import sqlite3
# python strings are immutable
buffer = create_string_buffer(b'hello', 15)
print(sizeof(buffer), repr(buffer.raw))


