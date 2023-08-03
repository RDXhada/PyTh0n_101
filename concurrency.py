# File/ DLL stuff
# code in the app
# import tavle
# export tavle

# concurrency 
# when two calculations do not have a obviously defined steps in evalutation/calculation

# threads for Python
# green threads - our code does the job for controlling
# system threads - the OS does the job for controlling

# one python process always works on one core

# fork - makes a new copy of the program that we are running
# resources and variables values are kept the same while running the process
# when creating the new process, all variables are local
# like cloning people, to do more work at the same time

# # fork example
# import os
# print('Before')
# if os.fork() : 
#     print('Father')
# else :
#     print('Son')
# print("Both")


# # harder example
# import time
def log(msg): print("\n* " + msg)
# orders = 0 
# while True:
#    order = input('Enter order: ')
#    if not order: continue
#    if order in ('q', 'x', 'quit', 'exit'): break 
#    pid = os.fork()
#    if pid == 0:
#     time.sleep(3)
#     log("Order '{0}' is ready!".format(order)) 
#     break
#    else:
#     log("Roger that '{0}'({1}). Please, wait.".format(order, orders)) 
#     orders += 1


# threads 
import threading
def f(name) :
    print("Hello from {0}".format(name))

thread = threading.Thread(target = f, args = ('Bob',))
thread.start()
thread.join()

# example 2 with threads

import time
orders = 0 
class Chef(threading.Thread) : 
    def __init__(self, order) : 
        self.order = order 
        threading.Thread.__init__(self)
    def run(self) :
        time.sleep(3)
        log("Order {0} is ready".format(self.order))


while True :
    order = input('Enter order : ')
    if not order : continue
    if order in ('q', 'x', 'quit', 'exit') : break
    chef = Chef(order)
    chef.start()
    log('Roger that {0}. Please wait...'.format(order))
    orders += 1