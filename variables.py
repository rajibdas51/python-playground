"""PI = 3.1416
a,b,c = 1,2,3
print(a,b)
# unpack a collection
fruits = ["apple","banana","cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)
"""
#global variable
"""
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) """

import sys
print(sys.version)
def myfunc():
  global x
  x = "fantastic"
  
myfunc()
 
print("Python is "+x)

if 5>2:
   print("five is greater than two!")