#Lists are used to store multiple items in a single variable.


newlist = ['apple','banana','mango']
print(newlist)

list1 = ["abc", 34, True, 40, "male"]

print(list1)

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


#It is also possible to use the list() constructor when creating a new list.

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist= list(('dog','cow','parrot'))


# access list items

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#-1 refers to the last item and -2 refers to the 2nd last item
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#You can specify a range of indexes by specifying where to start and where to end the range.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#To determine if a specified item is present in a list use the in keyword:



thislist = ["apple", "banana", "cherry"]

if "apple" in thislist :
    print("yes, apple is inthe fruits list!")