#A decorator is a function that takes another function as input and returns a new function.

#A basic decorator that uppercases the return value of the decorated function.

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

#A decorator can be called multiple times. Just place the decorator above the function you want to decorate.

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

#Arguments in the Decorated Function
