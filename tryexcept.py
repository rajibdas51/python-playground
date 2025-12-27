#The try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")


#  In this example, the try block does not generate any error:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  
#The finally block, if specified, will be executed regardless if the try block raises an error or not.


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")