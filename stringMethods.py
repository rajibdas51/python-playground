#Upper case the first letter in this sentence:
text = "hello, Everyone. Welcome to my blog."
x = text.capitalize()
print(x)

#Make the whole string lower case:

txt = "Hello Everyone!"
x= txt.casefold()
print(x)

#The center() method will center align the string, using a specified character (space is default) as the fill character.

txt = "bangladesh"
x = txt.center(30)
print(x)

#The count() method returns the number of times a specified value appears in the string.

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#The endswith() method returns True if the string ends with the specified value, otherwise False.

txt = "Hello, welcome to my world."
x= txt.endswith(",",0,6)
print(x)

""" The find() method finds the first occurrence of the specified value.

The find() method returns -1 if the value is not found."""

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

#The index() method finds the first occurrence of the specified value.

txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

#The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).

txt = "Company12"

x = txt.isalnum()

print(x)

#The isalpha() method returns True if all the characters are alphabet letters (a-z).


txt = "CompanyX"

x = txt.isalpha()

print(x)

#The upper() method returns a string where all characters are in upper case.


txt = "Hello my friends"

x = txt.upper()

print(x)


#Check if all the characters in the text are in lower case:

txt = "hello world!"

x = txt.islower()

print(x)

#Check if all the characters in the text are in upper case:

txt = "THIS IS NOW!"

x = txt.isupper()

print(x)

#The join() method takes all items in an iterable and joins them into one string.

myTuple = ("John", "Peter", "Vicky", "Natasha")

x = "#".join(myTuple)

print(x)

# convert the text to lower case
txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

# The replace() method replaces a specified phrase with another specified phrase.


txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

#The split() method splits a string into a list.

txt = "welcome to the jungle"

x = txt.split()

print(x)

#The strip() method removes any leading, and trailing whitespaces.

txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}

txt = "Hello Sam!"

print(txt.translate(mydict))