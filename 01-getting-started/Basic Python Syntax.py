#!/usr/bin/env python
# coding: utf-8

# # Basic Python Syntax

# ### 1. Hello world

# In[3]:


print("Hello world")


# ### 2. Variables and Assignments:
# Variables are containers for storing data values.
# A variable is created the moment you first assign a value to it.

# In[4]:


a = 10
b = -5.5

print(a)
print(b)


# Variables do not need to be declared with any particular type, and can even change type after they have been set.

# In[1]:


var0 = 100
var_1 = "Hello"

var_0 = "Hi"
var_1 = 50

print(var_0)
print(var_1)


# Variable name may:
# - Use upper-case and lower-case letters
# - Use numbers
# - Use underscore characters (an underscore is the _ character)
# 
# Variable name can **NOT**:
# - Use spaces
# - Start with a number
# 
# Variable names are case-sensitive.

# In[6]:


var, Var = 10, "abc"
print(var)
print(Var)

var, Var, Varr, varR = 10, "are", "abc", 90
print(Varr)
print(varR)

#10, abc, abc, 90


# ### 3. Comments
# Python has commenting capability for the purpose of in-code documentation.
# Comments start with a #, and Python will render the rest of the line as a comment:

# In[8]:


# This is a comment 1
# This is a comment 2

var = 10 # This is also a comment

"""
This is a comment
written in
more than just one line
"""


# ### 4. Data types
# In programming, data type is an important concept.
# 
# Variables can store data of different types, and different types can do different things.
# 
# Python has the following data types built-in by default, in these categories:
# 
# | Name | Notation |
# | --- | --- |
# | Text Type | str |
# | Numeric Types | int, float, complex |
# | Sequence Types | list, tuple, range |
# | Mapping Type | dict |
# | Set Types | set, frozenset |
# | Boolean Type | bool |
# | Binary Types | bytes, bytearray, memoryview |
# | None Type | NoneType |

# In[10]:


x = "Hello world" # str
x = 10            # int
x = 3.14          # float

x = ["apple", "banana", "cherry", "apple"] # list
x = ("apple", "banana", "cherry") # tuple

x = {                             # dict
        "name": "John",
        "age": 36
    }

x = {"apple", "banana", "cherry"} # set

x = True          # bool
x = False         # bool

x = None          # NoneType

x = 3.14


# In[11]:


print(type(x))


# #### Practice
# Create variables to store your name, age, and a favorite color. Print these variables using the print() function.

# In[21]:


name = "Nhu"
age = 19
color = "green"

print(name)
print(age)
print(color)


# ### 5. Casting
# There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
# 
# Casting in python is therefore done using constructor functions:
# 
# - `int()` - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# - `float()` - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# - `str()` - constructs a string from a wide variety of data types, including strings, integer literals and float literals

# In[17]:


x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3 

# Todo: Check their data type
print(type(x))
print(type(y))
print(type(z))


# In[18]:


x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# Todo: Check their data type
print(type(x), type(y), type(z), type(w))


# In[21]:


x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

# Todo: Check their data type
print(x, type(x))
print(y, type(y))
print(z, type(z))


# Cast a number type to string type (and vice versa). Then print them and check their data type.

# In[26]:


x = str(5)
y = float("11")

print(x, type(x))
print(y, type(y))


# ### 6. String
# 
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 
# `'hello'` is the same as `"hello"`.
# 
# You can display a string literal with the `print()` function:

# In[27]:


print("Hello, this is basic python")


# Assigning a string to a variable

# In[25]:


name = "Nhu"
print(name)


# To get the length of a string, use the len() function.

# In[26]:


name = "Hong Nhu"
print(len(name))


# To check if a certain phrase or character is present in a string, we can use the keyword `in`.

# In[33]:


txt = "The best things in life are free!"
print("free" in txt)
#print xem thử chữ free có nằm trong biến txt không

print("meo" in txt)


# Use it in an `if` statement:

# In[36]:


# Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

if "meo" not in txt:
    print("Chuc ban may man lan sau!")
    
if "meo" in txt:
    print("wrong")


# In[37]:


# Todo: Check if "expensive" is not in the variable txt:
if 'expensive' not in txt:
    print("expensive is not in the variable txt")


# ### 7. Print function

# Print a string

# In[38]:


print("Hello Nhu")


# Print variables

# In[39]:


name = "Hong Nhu"
age = 24
print(name, age)
print("Hello my name is ", name, " I'm ", age, " years old.")

#dấu phẩy không hiện ra ở outcome vì không include vào trong ""


# Print format string, an easy way to print a format string with other variables:

# In[40]:


print(f"Hello my name is {name}, I'm {age} years old.")
print("Hello my name is {name}, I'm {age} years old.")

#f là format


# ### 8. Arithmetic Operators
# 
# | Operator | Name | Example |
# | --- | --- | --- |
# | + | Addition | x + y |
# | - | Subtraction | x - y |
# | * | Multiplication | x * y |
# | / | Division | x / y |
# | % | Modulus | x % y |
# | ** | Exponentiation | x ** y |
# | // | Floor division | x // y |

# In[46]:


x = 5
y = 2

# Todo: perform all arithmetic operators:
print(f"{x} + {y} = {x+y}")
print(x, "+", y, "=", (x+y))

print(f"{x} - {y} = {x-y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} / {y} = {x/y}")
print(f"{x} % {y} = {x%y}")   # % là phép chia lấy phần dư, 5 chia 2 = 2 dư 1, kết quả = 1. 
print(f"{x} ** {y} = {x**y}") 
print(f"{x} // {y} = {x//y}") # phép chia lấy phần nguyên


# ### 9. User input
# Python allows for user input. That means we are able to ask the user for input.

# In[48]:


user_input = input()
print("User just typed: " + user_input)

abc = input()
print(abc)


# In[49]:


# Input function can be using with a prompt

name = input("What's your name? ")
print(f"Hello {name}!")

promt_to_ask = "How old are you? "
age = input(promt_to_ask)
age = int(age)      #lệnh này vì cần làm cho biến age được casting thành số nguyên, vì giá trị của input là string.
print(f"So you are {age}!")


# ------

# ## Practice:
# ### 1. Write a program that:
# - Input 2 number (int or float)
# - Print out the result of basic arithmetic operations (`+`, `-`, `*`, `/`, `%`)

# In[2]:


num_1 = input("write float number 1 here: ") #giá trị input luôn là 1 string, cho nên phải cast mới làm phép tính được
num_2 = input("write float number 2 here: ")
num_1 = float(num_1)
num_2 = float(num_2)
print(f"{num_1} + {num_2} = {num_1 + num_2}")
print(f"{num_1} - {num_2} = {num_1 - num_2}")
print(f"{num_1} * {num_2} = {num_1 * num_2}")
print(f"{num_1} / {num_2} = {num_1 / num_2}")
print(f"{num_1} % {num_2} = {num_1 % num_2}")  #2.5 chia 5 = 0 dư 2.5 


# ### 2. Create a Python program that calculates simple interest based on user input for principal amount, interest rate, and time.
# 
# - Prompt the user to enter the principal amount (initial amount).
# - Prompt the user to enter the annual interest rate.
# - Prompt the user to enter the time (in years).
# - Calculate the simple interest using the formula: `Simple Interest = (Principal * Rate * Time) / 100`
# - Display the calculated simple interest using the print() function.

# In[11]:


principal = input("Enter the principal amount: ")
interest = input("Enter the annual interest rate: ")
time = input("Enter the time (in years): ")
principal = float(principal)
interest = float(interest)
time = float(time)
print(f"Your simple interest is: {principal * interest * time / 100} euro") 

#trình bày zõ zàng cho user hiểu 


# ### 3. Write a program that converts temperatures between Celsius and Fahrenheit based on user input:

# In[8]:


"""
4 steps: 
1. Analysis: 
- convert C --> F 
- user input 
2. Design program
- user input (C)
- convert formula: F = (C × 9/5) + 32
3. Implement (code)
4. Test 
"""

tempt_c = input("Enter the temperature in Celsius: ")
tempt_c = float(tempt_c)
tempt_f = tempt_c * 9/5 + 32
print(f"{tempt_c}°C = {tempt_f}°F")


# ### 4. Write a program that ask personal info:
# - Name
# - Surname
# - Age
# - Major of study
# - 3 subjects of study and their marks
# 
# Print out the info and the average mark.

# In[15]:


name = input("Name: ")
surname = input("Surname: ")
age = input("Age: ")
major = input("Major of study: ")
sub_1 = input("Subject 1: ")
sub_1_mark = input(f"{sub_1} mark: ")
sub_2 = input("Subject 2: ")
sub_2_mark = input(f"{sub_2} mark: ")
sub_3 = input("Subject 3: ")
sub_3_mark = input(f"{sub_3} mark: ")
age = int(age)
sub_1_mark = float(sub_1_mark)
sub_2_mark = float(sub_2_mark)
sub_3_mark = float(sub_3_mark)
avg = (sub_1_mark + sub_2_mark + sub_3_mark)/3

print(f"The student information: {name} {surname}, {age} years old, {major}")
print(f"Three subjects of study and their marks:")
print(f"{sub_1}: {sub_1_mark}")
print(f"{sub_2}: {sub_2_mark}")
print(f"{sub_3}: {sub_3_mark}")
print(f"Average mark of three subjects is: {round(avg, 2)}")


# ### 5. Create a Python program that calculates the area of a circle based on user input for the radius.

# In[23]:


radius = input("Enter radius in cm: ")
radius = float(radius)
print(f"The area of the circle is: {3.14*(radius**2)} cm2")
print("Explanation: π * (radius^2)")
print("Note: π (pi) is a constant approximately equal to 3.14")


# ### 6. Create a Python program that calculates the Body Mass Index (BMI) based on user input for weight (in kilograms) and height (in meters).

# In[24]:


weight = input("Enter your weight(kg): ")
height = input("Enter your height(m): ")
weight = float(weight)
height = float(height)
bmi = weight/(height*height)
print(f"The Body Mass Index (BMI) is: {round(bmi, 2)} kg/m2")
print("Note: BMI = weight/(height*height)")


# ### 7. Create a Python program that calculates the area of a triangle based on user input for the base and height.

# In[25]:


base = input("Enter base (cm): ")
height = input("Enter height (cm): ")
base = float(base)
height = float(height)
triangle = (base*height)/2
print(f"The area of the triangle is: {round(triangle, 2)} cm2")
print("Explanation: (base*height)/2")

