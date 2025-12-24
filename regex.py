#Search the string to see if it starts with "The" and ends with "Spain":

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

#The findall() function returns a list containing all matches.

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)