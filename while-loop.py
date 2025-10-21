#The while Loop
i = 1
while i < 6:
  print(i)
  i += 1



# break statement
  i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


  #continue statement
  i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


#With the else statement we can run a block of code once when the condition no longer is true:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")