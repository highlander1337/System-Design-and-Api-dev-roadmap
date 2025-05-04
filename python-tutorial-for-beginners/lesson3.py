# About basic data types

name = "Tassio" # string data type
print(name, end=", ")
dialog = 'this "gentlemen" thinks that he\'s important.' # string with scape characters
print(dialog)
age = 10 # int data type
height = 1.4 # float data type
condition = age > 11 and height > 1.7 # bool data type
if condition is not True:
    print(f"But he's only {age} years old. And it's only {height} meters tall.")

print(type(name), type(dialog))
print(type(age))
print(type(height))
print(type(condition))

# More about python data types: https://www.w3schools.com/python/python_datatypes.asp

x = str("Hello World")
x = int(20)	
x = float(20.5)	
x = complex(1j)	
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)	
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)	
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))