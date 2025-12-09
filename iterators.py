#An iterator is an object that contains a countable number of values.
#Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#Strings are also iterable objects, containing a sequence of characters:

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


#Iterate the values of a tuple:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)



#Iterate the characters of a string:

mystr = "banana"

for x in mystr:
  print(x)