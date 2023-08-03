from typing import Any


class Snickers :
    def __init__(self, size, code) :
        self.size = size
        self.code = code

# we can use del to delete the atributes of an object
snickers = Snickers(25, "lol")
del snickers.size

class Hand : 
    # atribute of hand - variable
    figners_count = 5
    # atribute of hand - function/method
    def capitalize_finger(self, name) :
        setattr(self, name, getattr(self, name).upper())
    
    def __init__(self) :
        self.thumb = 'Палец' 
        self.index_finger = 'Показалец' 
        self.middle_finger = 'Среден' 
        self.ring_finger = 'Безименен' 
        self.pinkie = 'Кутре'

    def __getitem__(self, index) :
        return (self.thumb, self.index_finger, self.middle_finger, self.ring_finger, self.pinkie)[index]
    
    def __setitem__(self, index, value) : 
        if index == 0 :
            self.thumb = value
        elif index == 1 :
            self.index_finger = value

    def __getattr_(self, name) : 
        return f"Това е ръка v1.0. Все още няма {name} : ("
    
    def __setattr__(self, name, value):
        print(f"Нова стойнност за {name} - {value}")
        object.__setattr__(self, name, value)
    
    def __getattribute__(self,name) :
        print(f"Някой ми бърка по пръстите и иска {name}")
        return object.__getattribute__(self, name)
    
#if we dont use object.__seattr__ we might have a problem with endless recursion - overflow
# for example if we dont have object.__setattr__ and have 
# self.name = value we will have an overflow [endless recursion]
# we use __getattribute__ to call on every writing of an atribute


hand = Hand()
print(hand[0])

# convert 
hand[1] = 'кебабче'
print(hand.index_finger)
print(hand[1])
hand.pinkie = 'мАЛЪК ПрЪсТ'


# we can print an object as a dict or as a class atribute 
print(hand.__dict__)
print(hand.__class__)

# functions and variables defined inside the class are atributes of the class
print(Hand.figners_count)
print(Hand.capitalize_finger)
print(Hand.__dict__)  # output all atributes


# inheritance
class Limb :
    name = 'Limb'
    def __init__(self, name) : 
        print("Executing parent constructor.")
        self.name = name
    
    def introduce(self) :
        return f"I am a {self.name}"

class Leg(Limb) : 
    def introduce(self):
        return f"I am a {self.name}"
    pass

leg = Leg('leg')
print(leg.introduce())

class Hand1(Limb) :
    # we can use super
    def __init__(self, name):
        super().__init__(name)
        print('Executing child constructor')
        self.name = name
    def introduce(self) :
        return f"I am a {self.name}"
    
hand1 = Hand1('Ayo')
print(hand1.introduce())

class Animal :
    def __init__(self, animal, sound) :
        self.animal = animal
        self.sound = sound
        print(f"The {animal} is {sound}")

    def sing(self) :
        return f"{self.sound}".format(3)
    
cow = Animal('cow', 'moo-ing')

class Lion(Animal) :

    def __init__(self, sound) :
        self.sound = sound
    def sing(self) :
        return f"The Lion is {self.sound}"
    
lion = Lion('roaring')
print(lion.sing)

# composition is better than inheritance
# example
class Car :
    def __init__(self, brand):
        self.brand = brand

class Mercedes : 
    def __init__(self):
        self.brand = Car('Mercedes')


#mixins 
class NosePicker:
    def pick_nose(self):
        print('Извършвам действия, нужни за почистване на носа.')
class DriverAssistant:
    def assist_while_driving(self):
        print('Конфигурирам се за сигнализиране на останалите шофьори.')
class Scrather:
    def scratch(self):
        print('Почесвам всичко, което кажеш.')
class RingHolder:
    def wear_a_ring(self):
        print('Слагам си пръстен.')
class ForePlayer:
     def help_please_a_woman(self):
        print('Привеждам партньора си в готовност за забавления.')


class MiddleFinger(DriverAssistant, ForePlayer,Scrather) :
    def something(self) :
        print("something")

class IndexFinger(NosePicker, ForePlayer, Scrather) : 
    def something(self) :
        print("something")

# and again - encapsulation should be used carefully
# _name - protected
# __name - private

#bonus!
class Store :
    pass

class Lidl(Store) :
    pass

lidl = Lidl()
print(type(lidl) is Lidl) #true
print(type(lidl) is Store) #false
print(type(lidl)) # <class '__main__.Lidl'>
print(isinstance(lidl, Lidl)) # true
print(isinstance(lidl, Store)) # true
print(issubclass(Lidl, Store)) # true
print(issubclass(Store, Lidl)) # false