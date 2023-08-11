import streamlit as st

st.set_page_config(layout="wide")







st_hide="""
    <style> 
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(st_hide,unsafe_allow_html=True)


def code(text):
    st.code(text, language='python')




with st.sidebar:
    st.title("Python Wizards")
    st.markdown("**Coarse Elements**")
    Chapter = st.radio(
    "Chapters",
    ('Start','Hello World!', 'Data Storing', 'Data Types',"Basic Operators","Basic String Operations",'Conditions','Loops',"Functions",'Classes and Objects',"Modules and Packages"))
#`
if Chapter == "Start":
    st.title("Free python coarse!")
    st.markdown("This our free python coarse,to make a succeful journey with us you need to install [python](https://www.python.org/) or you can use an online compiler such as [programmiz](https://www.programiz.com/python-programming/online-compiler/?ref=26805f14) enjoy learning(:")
if Chapter == 'Hello World!':
    st.title("Hello World!")
    st.subheader("Python print() Function")
    st.markdown("""    The information displayed by the `print()` function is often in the form of lines, just like sentences in a paragraph. Each line can contain letters, numbers, or symbols, and they are shown one after another. To separate each line and make the output look neat, we use a special character called '\n' (newline) to mark the end of each line. It's like pressing the "Enter" key on the keyboard to start a new line when typing a document.
                        In summary, the `print()` function is a useful tool in Python that lets us display different types of information on the screen. It shows data like numbers and text, and the output is organized in lines, with each line separated by '`\\n`' which mean newline to make it easy to read.\n""")
    st.subheader("Example")
    code("print(\"Hello World\")")

    st.subheader("Result")
    code("Hello World")

if Chapter == 'Data Storing':
    st.title("Data Storing")
    st.subheader("Python Variables")
    st.markdown("Variables are places for storing values.")
    st.subheader("How to create a variable?")
    st.markdown("Python has no command for declaring a variable.")
    st.markdown("In order to create a variable you need first to state its name then put`=`sign then assign its value")
    st.subheader("Example")
    code("x = 5")
    st.markdown("Variables do not need to be declared with any particular type, and can even change type after they have been set.")
    code("""x = 4       # x is of type int
x = "Maria" # x is now of type str """)
    st.subheader("Casting")
    st.markdown("If you want to specify the type of a variable,it is done with casting.")
    code("""x = str(5)    # x will be '5'
y = int(5)    # y will be 5
z = float(5)  # z will be 5.0 """)
    st.subheader("Legal variables names")
    code("""myvar = "Hello"
my_var = "Hello"
_my_var = "Hello"
myVar = "Hello"
MYVAR = "Hello"
myvar2 = \"Hello\"""")
    st.subheader("Many Values to Multiple Variables")
    code("""x,y,z="Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
         """)
    st.subheader("Result")
    code("""
Orange
Banana
Cherry""")
if Chapter=="Data Types":
    st.title("Data Types")
    st.subheader("Most important Data Types")
    st.markdown("""
Text Type: 	`str`

Numeric Types: 	`int`, `float`
                
Sequence Types: 	`list`, `tuple`, `range`
                
Mapping Type: 	`dict`
                
Set Types: 	`set`
                
Boolean Type: 	`bool`
                
None Type: 	`NoneType`
                
""")
    st.subheader("Python Numbers")
    st.markdown("In programming,\"numbers\" data types refer to the various kinds of values that represent numerical quantities. These data types are essential for performing mathematical operations, calculations, and representing quantities in any programming language, including Python.")
    st.subheader("Example")
    code("""x = 1    # int which mean whole numbers
y = 2.8  # float which means decimal numbers""")
    st.subheader("Python Text")
    st.markdown("In programming, \"text\" data types refer to the ways in which textual information is stored, manipulated, and processed. Textual data is fundamental to a wide range of applications, from simple user interfaces to complex natural language processing tasks. ")
    st.subheader("Example")
    code("""x="Hello" #string which mean text
""")
    #`
    st.subheader("Python Sequence")
    st.markdown("In Python, \"sequence types\" are data types that represent ordered collections of items or elements. These types allow you to store multiple values in a specific order and access them using indexing. Python provides several built-in sequence types that serve different purposes. Here are the main sequence types in Python:")
    st.markdown("Lists (`list`): Lists are one of the most versatile sequence types. They are ordered collections of items that can be of different data types. Lists are mutable, meaning you can add, remove, or modify elements after creation. Lists are defined using square brackets `[]`.")
    st.subheader("Example")
    code("""fruits = ['apple', 'banana', 'orange']
numbers = [1, 2, 3, 4, 5]

# Modifying a list
fruits[1] = 'grape'
fruits.append('kiwi')

""")
    st.markdown("""Tuples (`tuple`):
Tuples are similar to lists but are immutable, meaning you cannot modify their elements after creation. Tuples are often used for grouping related data.""")
    code("""coordinates = (3.5, 2.8)
person = ('John', 25, 'john@example.com')

# Accessing elements
print(coordinates[0])  # Output: 3.5
""")
    
    st.markdown("""Range (`range`):
The `range` type represents an immutable sequence of numbers. It is commonly used for looping a specific number of times.""")
    st.subheader("Example")
    code("""# Generate a range of numbers from 1 to 10
number_range = range(1, 11)

# Convert the range object to a list
number_list = list(number_range)

print(number_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
""")
        #`

    st.subheader("Python Dictionaries")
    st.markdown("Dictionaries(`dict`) serve as containers for data values organized as key-value pairs. They are structured collections that maintain order*, can be modified, and prohibit the existence of duplicates.")
    st.subheader("Example")

    code("""
# Creating a dictionary to store information about a person
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York"
}

# Accessing values using keys
first_name = person["first_name"]
age = person["age"]

print("First Name:", first_name)  # Output: First Name: John
print("Age:", age)                # Output: Age: 30

# Modifying a value
person["age"] = 31
updated_age = person["age"]
print("Updated Age:", updated_age)        # Output: Updated Age: 31

""")  #`
    st.subheader("Python Sets")
    st.markdown("Sets(`set`) are used to store multiple items in a single variable.")
    st.subheader("Example")
    code("""thisset = {"apple", "banana", "cherry"}
print(thisset) # Output:{'cherry', 'banana', 'apple'}""")
    st.subheader("Python Boolean")

    
    st.markdown("A boolean in Python is like a light switch that can be either turned on (`True`) or off (`False`). It's used to make decisions in your code, like saying \"yes\" or \"no\" to questions.")
    st.subheader("Example")
    code("""
# Using booleans directly
is_light_on = True
is_door_open = False

# Printing boolean values
print("Is the light on?", is_light_on)
print("Is the door open?", is_door_open)
#Output:Is the light on? True
#Is the door open? False
""")
    st.subheader("Python NoneType")
    st.markdown("`None` is a special value that represents the absence of a value. It is often used to indicate that a variable or expression doesn't hold any meaningful data or that a function doesn't return any specific result.")
if Chapter==("Basic Operators"):
    st.title("Basic Operators")
    st.markdown("This section explains how to use basic operators in Python.")
    st.subheader("Math Operators")
    st.markdown("Just as any other programming languages, the addition, subtraction, multiplication, and division operators can be used with numbers.")
    st.subheader("Example")
    code("""number = 1 + 2 * 3 / 4.0
print(number)#Output:2.5
""")
    st.markdown("Another operator available is the modulo (%) operator, which returns the integer remainder of the division. dividend % divisor = remainder.")
    code("""remainder = 11 % 3
print(remainder) #Output:2""")
    st.markdown("Using two multiplication symbols makes a power relationship.")
    code("""
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)
         """)
    st.subheader("Using Operators with Strings")
    st.markdown("Python supports concatenating strings using the addition operator:")
    code("""
helloworld = "hello" + " i" + "world"
print(helloworld) #Output:helloiworld

""")
if Chapter=="Basic String Operations":
    st.title("Basic String Operations")
    st.subheader("Len function")
    st.markdown("""
The `len()` function in Python is used to find the length (number of elements) of a sequence, such as a string, list, or tuple. Here's a simple example using a string:

```python
text = "Hello, World!"
length = len(text)

print("The length of the text is:", length)  # Output: The length of the text is: 13
```

In this example, the `len()` function is used to determine the number of characters in the string `text`, which is "Hello, World!". The length of this string is 13 characters, so the output will be "The length of the text is: 13".
""")
    st.markdown("""
I apologize for the confusion. It seems you're referring to the `index()` method in Python, which is used to find the index (position) of a specified value within a list. Here's a simple example:

```python
numbers = [10, 20, 30, 40, 50]

# Finding the index of a value
index_of_30 = numbers.index(30)
print("Index of 30:", index_of_30)  # Output: Index of 30: 2
```

In this example, the `index()` method is used to find the index of the value `30` within the list `numbers`. Since `30` is at index `2` in the list, the output will be "Index of 30: 2". If the value is not found, this method will raise a `ValueError`.

""")
if Chapter=="Conditions":
    st.title("Conditions")
    st.markdown("""
Let's delve into the basics of conditional statements in Python.

**Conditional Statements:**

Conditional statements are used in programming to make decisions based on certain conditions. In Python, the primary conditional statements are:

1. **if Statement:**
   The `if` statement is used to execute a block of code only if a given condition is `True`.

   ```python
   age = 18
   if age >= 18:
       print("You are an adult.")
   ```

2. **if-else Statement:**
   The `if-else` statement allows you to execute one block of code if a condition is `True`, and another block if the condition is `False`.

   ```python
   age = 15
   if age >= 18:
       print("You are an adult.")
   else:
       print("You are not an adult yet.")
   ```

3. **if-elif-else Statement:**
   The `if-elif-else` statement lets you check multiple conditions and execute different blocks of code based on the condition that evaluates to `True`.

   ```python
   score = 85
   if score >= 90:
       print("You got an A.")
   elif score >= 80:
       print("You got a B.")
   elif score >= 70:
       print("You got a C.")
   else:
       print("You need to improve.")
   ```

**Logical Operators:**

Logical operators help you create more complex conditions by combining multiple conditions. The primary logical operators in Python are:

- `and`: Returns `True` if both conditions are `True`.
- `or`: Returns `True` if at least one condition is `True`.
- `not`: Reverses the logical outcome of a condition.

**Nested Conditions:**

You can also nest conditional statements within each other to handle more intricate decision-making scenarios.

Here's an example that combines these concepts:

```python
temperature = 28
is_raining = True

if temperature > 30 and not is_raining:
    print("Go to the beach!")
elif temperature > 25 or is_raining:
    print("Stay indoors.")
else:
    print("Enjoy a walk outside.")
```

In this example, the program checks temperature and rain conditions to provide different suggestions based on the values.

Remember that indentation is crucial in Python to define the scope of code blocks within conditional statements. The code under each condition is indented to indicate what should be executed when that condition is met.

Feel free to experiment with these concepts to build a better understanding of how Python's conditional statements work.
""")
if Chapter=="Loops":
    st.title("Loops")
    st.markdown("""
In Python, loops are used to execute a block of code repeatedly. They allow you to automate tasks by iterating through collections or running code as long as a specific condition is met. There are two main types of loops in Python: `for` loops and `while` loops.
**for Loop Syntax:**

```python
for element in sequence:
    # Code block to execute for each element
```

Example:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**for Loop Control Statements:**

- `break`: Terminates the loop prematurely when a certain condition is met.
- `continue`: Skips the current iteration of the loop and proceeds to the next one.
- `pass`: Acts as a placeholder for an empty loop or a loop that you plan to fill in later.

Example:

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break  # Exit the loop when num is 3
    print(num)
```

**Nested for Loops:**

```python
for outer_item in outer_sequence:
    for inner_item in inner_sequence:
        # Code block to execute for each combination of outer_item and inner_item
```

Example:

```python
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")
```

**while Loop Syntax:**

```python
while condition:
    # Code block to execute as long as the condition is True
```

Example:

```python
count = 0
while count < 5:
    print("Count:", count)
    count += 1
```

**while Loop Control Statements:**

- `break`: Terminates the loop prematurely when a certain condition is met.
- `continue`: Skips the current iteration of the loop and proceeds to the next one.
- `pass`: Acts as a placeholder for an empty loop or a loop that you plan to fill in later.

Example:

```python
x = 0
while x < 3:
    if x == 1:
        x += 1
        continue  # Skip the rest of the loop body for x = 1
    print(x)
    x += 1
```

**Nested while Loops:**

```python
while outer_condition:
    while inner_condition:
        # Code block to execute for each combination of outer_condition and inner_condition
```

Example:

```python
i = 0
while i < 3:
    j = 0
    while j < 2:
        print(f"({i}, {j})")
        j += 1
    i += 1
```

Feel free to experiment with these concepts in your Python interpreter or script to reinforce your understanding of loops and their various features.

""")
if Chapter=="Functions":
    st.title("Functions")
    st.markdown("""
**Functions:**

Functions in Python are blocks of reusable code that perform specific tasks. They help organize your code, make it more modular, and allow you to avoid repetitive coding. Functions take input arguments, perform actions based on those arguments, and often return a value.

**Defining a Function:**

You define a function using the `def` keyword followed by the function name and a pair of parentheses. You can also define input parameters within the parentheses. The function body is indented and contains the code to be executed.

```python
def greet(name):
    print("Hello, " + name + "!")
```

**Calling a Function:**

To use a function, you call it by its name followed by parentheses. If the function has parameters, you provide the values within the parentheses.

```python
greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
```

**Returning Values:**

Functions can also return values using the `return` statement. The value can be used in other parts of your code.

```python
def add(a, b):
    return a + b

result = add(5, 3)
print("Result:", result)  # Output: Result: 8
```

**Default Parameters:**

You can assign default values to parameters in a function. If a value isn't provided when the function is called, the default value will be used.

```python
def greet(name="Guest"):
    print("Hello, " + name + "!")

greet()          # Output: Hello, Guest!
greet("Alice")   # Output: Hello, Alice!
```

**Variable Number of Arguments:**

Functions can take a variable number of arguments using the `*args` syntax. These arguments are collected into a tuple.

```python
def display_args(*args):
    for arg in args:
        print(arg)

display_args("apple", "banana", "cherry")
# Output:
# apple
# banana
# cherry
```

**Keyword Arguments:**

You can pass arguments using their parameter names, which allows you to specify arguments out of order.

```python
def show_info(name, age):
    print("Name:", name)
    print("Age:", age)

show_info(age=25, name="Alice")
# Output:
# Name: Alice
# Age: 25
```

**Docstrings:**

You can add docstrings (documentation strings) within a function using triple quotes. These provide a description of the function's purpose, usage, and parameters.

```python
def square(number):
    \"""
    Returns the square of a number.
    
    :param number: The number to be squared.
    :return: The square of the number.
    \"""
    return number ** 2
```

Using functions helps make your code more organized, modular, and easier to maintain. It's an essential concept in programming that promotes code reusability and readability.
""")
if Chapter=="Classes and Objects":
    st.title("Classes and Objects")
    st.markdown("""
**Classes and Objects:**

In Python, a class is a blueprint for creating objects. Objects are instances of classes. Classes define the attributes (data) and methods (functions) that objects of that class will have.

**Defining a Class:**

You define a class using the `class` keyword followed by the class name. The class body contains attributes and methods.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name + " says woof!")
```

**Creating Objects:**

To create an object from a class, you call the class as if it's a function. This is called instantiation.

```python
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 2)
```

**Accessing Attributes and Methods:**

You can access attributes and methods of an object using dot notation.

```python
print(dog1.name)    # Output: Buddy
print(dog2.age)     # Output: 2
dog1.bark()         # Output: Buddy says woof!
```

**Constructor (`__init__`):**

The `__init__` method is a special method (also known as a constructor) that gets called when an object is created. It's used to initialize the object's attributes.

**Methods:**

Methods are functions defined inside a class that operate on the object's attributes.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print("Circle Area:", circle.area())  # Output: Circle Area: 78.5
```

**Inheritance:**

Inheritance allows you to create a new class based on an existing class. The new class inherits attributes and methods from the existing class.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
```

**Encapsulation:**

Encapsulation refers to restricting access to certain attributes or methods. By convention, attributes with a single underscore `_` prefix are considered "protected," and attributes with a double underscore `__` prefix are considered "private."

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected attribute

    def deposit(self, amount):
        self._balance += amount

account = BankAccount(100)
account.deposit(50)
print("Balance:", account._balance)  # Output: Balance: 150
```

Classes and objects provide a way to model real-world concepts and actions, leading to more organized and modular code. It's a fundamental concept in object-oriented programming that enhances code structure and reusability.

""")
if Chapter=="Modules and Packages":
    st.title("Modules and Packages")
    st.markdown("""
**Modules:**

Modules in Python are files containing Python code, typically consisting of functions, classes, and variables. They help organize and manage code by breaking it into smaller, manageable parts.

**Creating a Module:**

1. Create a new `.py` file containing your code.
2. In your main script, use the `import` keyword to include the module.

**Example: `my_module.py`**

```python
def greet(name):
    print("Hello, " + name + "!")
```

**Using a Module:**

```python
import my_module

my_module.greet("Alice")  # Output: Hello, Alice!
```

**Packages:**

Packages are collections of modules organized in directories. They provide a hierarchical structure to manage and categorize related modules.

**Creating a Package:**

1. Create a directory for your package.
2. Inside the package directory, create `.py` files as modules.
3. In your main script, use the `import` keyword to include modules from the package.

**Example: Directory Structure**

```
my_package/
│
├── __init__.py
├── module1.py
└── module2.py
```

**Using a Package:**

```python
import my_package.module1

my_package.module1.some_function()
```

**Importing Specific Items:**

You can import specific functions, classes, or variables from a module/package using the `from` keyword.

```python
from my_module import greet

greet("Bob")  # Output: Hello, Bob!
```

**Aliases:**

You can use aliases to give modules or packages shorter names for convenience.

```python
import my_module as mm

mm.greet("Charlie")  # Output: Hello, Charlie!
```

**Third-party Packages:**

Python has a rich ecosystem of third-party packages available through the Python Package Index (PyPI). You can install these packages using tools like `pip`.

**Example: Installing and Using `requests` Package**

```python
# Install the package
# pip install requests

# Import and use the package
import requests

response = requests.get("https://www.example.com")
print("Status Code:", response.status_code)
```

Modules and packages help you organize, reuse, and distribute your code effectively. They're an essential part of building maintainable and modular programs in Python.

""")