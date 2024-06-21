#!/usr/bin/env python
# coding: utf-8

# ### Qstn 1: Write a program in Python to show all levels of Inheritance.

# In[12]:


# Base class for single-level, multi-level, and hierarchical inheritance
class Animal:
    def sound(self):
        return "Some generic sound"

# Single-Level Inheritance
class Dog(Animal):
    def sound(self):
        return "Bark"

# Multi-Level Inheritance
class Puppy(Dog):
    def sound(self):
        return "Small bark"

# Classes for multiple inheritance
class generic_species:
    def bark(self):
        return "Bark"

class Pet:
    def is_pet(self):
        return True

# Multiple Inheritance
class Bulldog(generic_species, Pet):
    def breed(self):
        return "Bulldog"

# Hierarchical Inheritance
class Cat(Animal):
    def sound(self):
        return "Meow"

# Testing all levels of inheritance

# Single-Level Inheritance
dog = Dog()
print("Single-Level Inheritance: Dog:", dog.sound())  

# Multi-Level Inheritance
puppy = Puppy()
print("Multi-Level Inheritance: Puppy:", puppy.sound())  

# Multiple Inheritance
bulldog = Bulldog()
print("Multiple Inheritance: Bulldog:", bulldog.bark(), "-", bulldog.is_pet(), "-", bulldog.breed())  

# Hierarchical Inheritance
cat = Cat()
print("Hierarchical Inheritance: Cat:", cat.sound())  


# ### Qstn 2: Write a program in Python to show Method Overloading.
# #### Ans:- Some explanation: Method overloading refers to the ability to create multiple methods in the same class, all having the same name but different parameters (either in number or type). It allows a class to perform a single action in different ways. 
# - Here is an example:

# In[13]:


class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Creating an instance of Calculator
calc = Calculator()

# Testing method overloading
print(calc.add(2))          # one argument
print(calc.add(2, 3))       # two arguments
print(calc.add(2, 3, 4))    # three arguments


# ### Qstn 3: Write a program in Python to show Method Overriding.
# #### Ans:- Some explanation: Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The method in the subclass should have the same name, same parameters, and same return type as the method in the superclass.
# #### Below is the code:

# In[14]:


# Superclass
class Animal:
    def sound(self):
        return "Generic sound"

# Subclass Dog overrides the sound method
class Dog(Animal):
    def sound(self):
        return "Bark"

# Subclass Cat overrides the sound method
class Cat(Animal):
    def sound(self):
        return "Meow"

# Creating instances of each class
animal = Animal()
dog = Dog()
cat = Cat()

# Demonstrating method overriding
print(animal.sound())  
print(dog.sound())             
print(cat.sound())             

