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

#The clear() method empties the list.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#You can loop through the list items by using a for loop:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


  thislist = ["apple", "banana", "cherry"]
  for i in range(len(thislist)):
     print(thislist[i])

#You can loop through the list items by using a while loop.

  thislist = ["apple", "banana", "cherry"]
  i =0
  while i< len(thislist):
     print(thislist[i])
     i = i+1


thislist = ["apple", "banana", "cherry"]

[print(x) for x in thislist]


#Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# sort number
thislist = [100, 50, 65, 82, 23]

thislist.sort()

print(thislist)


#To sort descending, use the keyword argument reverse = True:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=true)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Append list2 into list1:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

