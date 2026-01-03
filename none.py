#None is a special constant in Python that represents the absence of a value.
#Variables can be assigned None to indicate "no value" or "not set".

x = None
print(x)
x = None
print(type(x))

#Use the identity operator is for comparisons with None:

result = None
if result is None:
  print("No result yet")
else:
  print("Result is ready")