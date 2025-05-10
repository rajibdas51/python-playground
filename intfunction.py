"""
The Python int() function converts a given object to an integer or converts a decimal (floating-point) number to its integer part by truncating the fractional part.
"""
age ="21"

print("age =", int(age))
print("int(9.9)",int(9.9))

print("int(9)=", int(9))

# octal to decimal using int()
print("int() on 0o12 =", int('0o12', 8))

# binary to decimal using int()
print("int() on 0b110 =", int('0b110', 2))

# hexa-decimal to decimal using int()
print("int() on 0x1A =", int('0x1A', 16))

