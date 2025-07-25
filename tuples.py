#A tuple is a collection which is ordered and unchangeable.

thistuple = ("apple", "banana", "cherry")
print(thistuple)


#One item tuple, remember the comma:


thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#String, int and boolean data types:


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)


#A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")

#From Python's perspective, tuples are defined as objects with the data type 'tuple':


mytuple = ("apple", "banana", "cherry")

print(type(mytuple))

#Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative indexing means start from the end.

#-1 refers to the last item, -2 refers to the second last item etc.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#You can specify a range of indexes by specifying where to start and where to end the range.

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#By leaving out the start value, the range will start at the first item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#To determine if a specified item is present in a tuple use the in keyword:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")