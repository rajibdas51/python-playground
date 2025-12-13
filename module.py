#To create a module just save the code you want in a file with the file extension .py
#Save this code in a file named mymodule.py

def greeting(name):
  print("Hello, " + name)


#Import the module named mymodule, and call the greeting function:

import mymodule

mymodule.greeting("Jonathan")

#The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):


#Save this code in the file mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#Import the module named mymodule, and access the person1 dictionary:

import mymodule

a = mymodule.person1["age"]
print(a)


#You can create an alias when you import a module, by using the as keyword:
#Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)


#List all the defined names belonging to the platform module:

import platform

x = dir(platform)
print(x)


#The module named mymodule has one function and one dictionary:

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}