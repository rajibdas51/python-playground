# multiple string in single variable
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Looping through string
str= "Banana"
for x in str:
   print(x)

# string length
print(len(str))

# check if a certain phrase or character is present in a string
txt = "I love my Country"
print("love" in txt)

# print only if 'love' is exist in txt

if "love" in txt:
   print("I love my country!")

#To check if a certain phrase or character is NOT present in a string
print("Bangladesh" not in str)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#Display the value 95 with 2 decimals:

txt = f"The price is {95:.2f} dollars"
print(txt)

#Add taxes before displaying the price:

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)