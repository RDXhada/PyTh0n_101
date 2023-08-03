# before the topic
# when we check for equality of numbers we use ==
# when we want to check if the objects are the same we use "is"
# basically if the references are the same
a = 3**20
b = 3
print(a is b)

print(5 % 5 or 'lmao')


# if we use 'for' we should use enumerate
nums = [12,3,4,5,6]
for i, num in enumerate(nums) :
    if num % 4 == 0 :
        i += 1
    else :
        i += 2

# ternary operator
# bad implementation
number = 12
if number % 3 == 0 :
    divisor = 3
else :
    divisor = 5

# good implementation
divisor = 4 if number % 3 == 0 else 5

# chaining 
# bad
angle = 105
if angle > 0 and angle < 90 : 
    print('angle is in first quadrant')

# good
if 90 < angle <= 180 :
    print('angle is in second quadrant')



# EXCEPTIONS (PART 7)
class MadWife(Exception) : 
    wife = 'she is very mad'
    """exception raised by mad wife"""

# we can have all kinds of exceptions - syntax erros
# we use raise to force an exception
# or to throw an exception basically
x = 3
if x > 10 :
    raise Exception('X SHOULD NOT BE MORE THAN 10. THE VALUE CURRENTLY IS {}'.format(x))

# in windows this will result in error
import sys
# assert('linux' in sys.platform), 'This code runs on Linux only!'

# handling exceptions
def linux_interaction() : 
    assert('linux' in sys.platform), 'Function that can only run in linux platforms'
    print("Do something pls woof woof")

try :
    linux_interaction()
except AssertionError as error :
    print(error)
    print('linux functions was not executed!')
# in windows/mac this will output :
# Function can only run on Linux systems.
# The linux_interaction() function was not executed


try : 
    with open('lolol.png') as file :
        read_data = file.read() 
except FileNotFoundError as fnf_error : 
    print(f"Could not open file. Error is : {fnf_error}")
except AssertionError as error:
    print(error)
    print('Linux linux_interaction() function was not executed')

# else clause
try :
    linux_interaction()
except AssertionError as error :
    print(f"Error is {error}")
else :
    print("Executing the else clause")


try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(f"In else clause [{fnf_error}]")
finally:
    print('Cleaning up, irrespective of any exceptions.')

# raise allows us to throw an exception at any time
# assert enables us to verify certain conditions 
# in the try clause, all statements are executed until an exception is encountered
# except is used to catch and handle the exceptions
# else lets you code sections that should only run when no exceptions are encountered in the try clause
# finally executes sections fo code that should always run - with or without any previous encountered exceptions

# EAFP - easier to ask for forgiveness than permission
# if not box.empty() :
#     box.pick_item()
# try :
#     box.pick_item()
# except :
#     <someone can fill up the box>


# LBYL - look before you leap
# if not box.empty() and not box.locked() :
#     box.pick_item() 
# try :
#     box.pick_item()
# except BoxLockedError :
#     <too late>



class MadWifeError(Exception):
    """Exception raised by a mad wife."""
    def __init__(self, message='Ядосана съм и ти си знаеш защо.'): 
        self._message = message
        super().__init__(self._message)
    def __str__(self):
        return f'Глупак, простак, мръсник, циник! {self._message}'

# raise MadWifeError() # throw the exception

# when do we not use try except? (part 1)
try :
    print('Going outside')
except MadWifeError :
    raise RuntimeError('Wife is mad')
# we should have more information about the error!

# when do we not use try except? (part 2)
# when we cannot handle/plan for the specific error
def homework(text) :
    try :
        return text.split()
    except AttributeError :
        return None
    
print(homework(666))

# def homework(text) :
#     return text.split()

# print(homework(777)) this will result in error


# learning 'with'
# with open('C:/users/lmao' as source_file) 

# little exercise
class Recipient:
    def __init__(self, name):
        self.name = name
    
    def await_response(self) :
        return f"Тук {self.name}. Прието. Край."



class AlloAlloConversation :
    def __init__(self, name) :
        self._name = name

    def __enter__(self) :
        print(f"Ало-ало, тук {self._name}")
        return Recipient('Лондон')
    def __exit__(self, type, value, traceback) :
        print('И точка.')

    
class AlloAlloMessage:
    def __init__(self, recipient_name):
        self._recipient_name = recipient_name
    def __enter__(self): 
        print(f"{self._recipient_name}, "
              "предавам закодирано съобщение:") 
        
    def __exit__(self, type, value, traceback):
        print("Край.")


with AlloAlloConversation("Нощен ястреб") as recipient: 
    with AlloAlloMessage(recipient.name) :
        print('Английските летци са на лекция във ФМИ.') 
    print(recipient.await_response())
with AlloAlloMessage(recipient.name):
    print('Никой от тях не е гледал сериала и не разбират за какво говоря.')