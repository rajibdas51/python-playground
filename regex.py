#Search the string to see if it starts with "The" and ends with "Spain":


import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

#The findall() function returns a list containing all matches.

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#Search for the first white-space character in the string:

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#Split at each white-space character:

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)