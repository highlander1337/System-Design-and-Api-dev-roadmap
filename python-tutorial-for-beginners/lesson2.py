# Print any data to the console
data = 10
print(data)

# Print with a separator
print("Nome", "Sorenome", sep=" | ")

# Print with a end character
print(10, end=".0000\n")

# Print will print end if no args are given
print(end=".0000\n") # Change end to custom logic

# More examples with print
print("Hello", "World", sep="-", end="!\n") # Combining sep and end
print(f"Data: {data}") # Presenting data to the real world

# Complex example to print data into a file
# with open("python-tutorial-for-beginners\data.txt", "w") as text_file:
#     print(f"{data}", file=text_file, end="\n")
# See more in https;://docs.python.org/3/library/functions.html#print