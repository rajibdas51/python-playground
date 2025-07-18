fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

#With list comprehension you can do all that with only one line of code:
newlist = [x for x in fruits if "a" in x]

print(newlist)
newlist = [x for x in fruits if x != "apple"]

print(newlist)

#You can use the range() function to create an iterable:

newlist = [x for x in range(10)]
#Accept only numbers lower than 5:


newlist = [x for x in range(10) if x < 5]

#Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]