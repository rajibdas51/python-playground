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



    # Change list items

    #change item value
    thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#The insert() method inserts an item at the specified index:



thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist)

#To add an item to the end of the list, use the append() method:

thislist = ["apple","Banana", "cherry"]
thislist.append("orange")
print(thislist)


#To append elements from another list to the current list, use the extend() method.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


#Remove the first occurrence of "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely.



thislist = ["apple", "banana", "cherry"]
del thislist