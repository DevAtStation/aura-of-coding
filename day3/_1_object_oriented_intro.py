# (DETAILED CLASS AND OBJECT SYNTAX EXPLANATION AT THE END OF THE FILE)
# Object Oriented Programming Intro:
# OOP is a way of thinking about programming, based on the concept of "objects", which can contain data, in the form of variables, often known as attributes; and code, in the form of functions, often known as methods.
# You may think of attributes as the things the object has, and the methods as the things the object can do.

# Let's take a car for example:
class Car: 
    def __init__(self):
        self.color = ""
        self.year = 0

    def honk(self):
        print("Honk!")
    
    def drive(self):
        print("The car is driving")

# blue_car = Car()
# blue_car.color = "Blue"
# blue_car.year = 2010
# blue_car.honk()

# Animal class
class Animal:  # this is the parent class 
    def __init__(self, name, age): # this is the constructor
        self.name = name
        self.age = age

    def speak(self): # this is a method
        print("Doesn't make any sound")

class Dog(Animal):
    def __init__(self, name, breed, hair_type, age):
        super().__init__(name, age) # this will call the constructor from the parent class
        self.breed = breed
        self.hair_type = hair_type
    
    def run(self):
        print("The dog is running")

    def speak(self):
        print("Woof!") # this will override the speak method from the parent class

    def description(self):
        print(f"{self.name} is a {self.breed} that is {self.age} years old")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age) # this will call the constructor from the parent class
    
    def speak(self):
        print("Meow!") # this will override the speak method from the parent class

class StingRay(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

def make_animal_speak(animal):
    animal.speak() # this will call the speak method from the class that the animal is an instance of

big_dog = Dog("Skamp", "Rothweiler", "short", 9)
make_animal_speak(big_dog) # this will call the speak method from the Dog class
normal_cat = Cat("Snowball", 5)
make_animal_speak(normal_cat) # this will call the speak method from the Cat class
sting_ray = StingRay("Stingy", 1)
make_animal_speak(sting_ray) # this will call the speak method from the Animal class

print("")
# big_dog.age = 10
# big_dog.description()

# big_dog2 = big_dog
# big_dog2.age = 3
# big_dog2.description()
# big_dog2.bark()
# big_dog2.run()
# print(big_dog2.hair_type)


class Person:
    def __init__(self, firstname, lastname, age, job, sex):
        self.firstname = firstname 
        self.lastname = lastname
        self.age = age
        self.job = job
        self.sex = sex

    def description(self):
        print(f"{self.firstname} {self.lastname} is a {self.sex} {self.job} who is {self.age} years old")


# viktor = Person("Viktor", "Shep", 27, "barista", "male")
# viktor.description()
# print("")
#X3


class Henchman:
    count = 0
    active_count = 0
    dead_henchs = 0

    def __init__(self):
        Henchman.count += 1
        Henchman.active_count += 1

        if Henchman.count == 1:
            self.name = "Dr Girlfriend"
        elif Henchman.count == 5:
            self.name = "Gary"
        else:
            self.name = f"Henchman #{Henchman.count}"
        self.is_dead = False

    def die(self):
        if self.is_dead:
            return
        Henchman.dead_henchs += 1
        Henchman.active_count -= 1
        self.is_dead = True
        print(f"{self.name} died!")
    
    def say_hello(self):
        print(f"{self.name} said hello")

hench_1 = Henchman()
hench_2 = Henchman()
hench_3 = Henchman()
hench_4 = Henchman()
hench_5 = Henchman()
hench_1.say_hello()
hench_2.say_hello()
hench_3.say_hello()
hench_4.say_hello()
hench_5.say_hello()
hench_2.die()
hench_3.die()
hench_4.die()
print(f"The total number of henchs is {Henchman.count}")
print(f"The total number alive henchs is {Henchman.active_count}")
print(f"The total number of killed henchs is {Henchman.dead_henchs}")
print("")

import json
test = json.dumps(hench_1.__dict__, indent=4)
print(test)


# class is a blueprint for creating objects, it contains all the methods and attributes of the object, e.g. class Object has the method method() and the attribute attribute
class Object: 
    # The __init__() method is a special method, which is called class constructor or initialization method that Python calls when you create a new instance of this class.
    # It is called automatically every time the class is being used to create a new object.
    def __init__(self):
        # attribute is a variable that belongs to the object, and is accessible through the object, e.g. object.attribute = 1 sets the attribute to 0, it can of any type, e.g. int, float, string, list, etc.
        self.attribute = 0

    def method(self): # method is a function that belongs to the object, and is accessible through the object, e.g. object.method() calls the method
        # self is a reference to the current instance of the class, and is used to access variables that belong to the class
        self.attribute += 1

# object = Object() # object is an instance of the class Object, it is created using the class name as a function
# print(object.attribute) # prints the attribute of the object, Output: 0
# object.method() # calls the method of the object
# print(object.attribute) # prints the attribute of the object, Output: 1