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