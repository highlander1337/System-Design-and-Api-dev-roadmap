# This is a single-line comment.
# It explains what the following line of code is intended to do.

"""
This is a docstring.
Docstrings provide important information about the purpose, inputs, and outputs
of functions, methods, or classes.

See PEP 0257 for more information on docstrings:
https://peps.python.org/pep-0257/

Should be noticed that docstrings aren't comments, they are multiple line
strings that was not assigned to any variable. So it will be ignored at 
runtime.

According to the Python PEP 8 Style Guide, there are several things to keep in mind while writing comments:

1. Comments should always be complete and concise sentences.
2. It’s better to have no comment at all than one that’s difficult to understand or inaccurate.
3. Comments should be updated regularly to reflect changes in your code.
4. Too many comments can be distracting and reduce code quality. Comments aren’t needed where the code’s purpose is obvious.

Reference: https://peps.python.org/pep-0008/


Furthemore, comments can provide content for our documentation by using document generators like https://www.sphinx-doc.org/en/master/.

"""


def print_hello_world():
    """
        This function prints the classic phrase "Hello, World!" to the console.
        It does not return any value.
        
        Arguments:
        None
    """
    # Store the message "Hello, World!" in a variable
    message = "Hello, World!"
    # Print the message to the console
    print(message)

print_hello_world()


""" 
5 Simple rules, ref: https://kinsta.com/blog/python-comments/

1. Avoid the obvious

x1 = 0
# Bad comment
x1 = x1 + 4 # Increase x by 4

x2 = 0
# Good comment
x2 = x2 + 4 # Increase the border width

2. Keep it simple

# Bad comment
# return area by performing, Area of cylinder = (2*PI*r*h) + (2*PI*r*r)
def get_area(r,h):
    return (2*3.14*r*h) + (2*3.14*r*r)

# Good comment
# return area of cylinder
def get_area(r,h):
    return (2*3.14*r*h) + (2*3.14*r*r)
    
3. Use indentifiers carefully

# Bad comment
# return class() after modifying argument
def func(cls, arg):
    return cls(arg+5)
    
# Good comment
# return cls() after modifying arg
def func(cls, arg):
    return cls(arg+5)
    
4. DRY (Don't Repeat Yourself) and avoid WET (Write Everything Twice)

# Bad comment
# function to do x work
def do_something(y):
    # x work cannot be done if y is greater than max_limit
    if y < 400:
      print('doing x work')

# Good comment
# function to do x if arg:y is less than max_limit
def  do_something(y):
    if y in range(400):
        print('doing x work')

5. Consistent identation

# Bad comment
for i in range(2,20, 2):
# only even numbers
    if verify(i):
# i should be verified by verify()
        perform(x)
        
# Good comment
# only even numbers
for i in range(2,20, 2):
    # i should be verified by verify()
    if verify(i):
        perform(x)

"""



