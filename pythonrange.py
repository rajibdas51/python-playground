#Creating ranges
range(start,stop,step)
x = range(10)

#Create a range of numbers from 3 to 9:
x = range(3, 10)

#Iterate over each value in a range:

for i in range(10):
  print(i)


#Convert different ranges to lists:

print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))

#Extract a subsequence from a range:

r = range(10)
print(r[2])
print(r[:3])

#Test if the numbers 6 and 7 are present in a range:

r = range(0, 10, 2)
print(6 in r)
print(7 in r)


#Get the length of a range:

r = range(0, 10, 2)
print(len(r))