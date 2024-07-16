# While Loop

count = 0
while count < 3:
    count += 1
    print("Hello Geek")


# Single statement while block:

count = 0
while count == 2:
    print("Hello Geek")


# for in Loop:

l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)


print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)


# Continue Statement:

for letter in "geeksforgeeks":
    if letter == "e" or letter == "s":
        continue
print("Current Letter :", letter)


# Break Statement:
for letter in "geeksforgeeks":
    if letter == "e" or letter == "s":
        break
print("Current Letter :", letter)


# Creating a Function


def my_function():
    print("Hello from a function")


my_function()


# Parameters


def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Default Parameter Value


def my_function(country="Norway"):
    print("Iam from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Passing a List as a Parameter


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)


# Return Values


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


# Keyword Arguments


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# Create Class and Object


class Dog:
    def bark(self):
        print("Woof!")


my_dog = Dog()

my_dog.bark()


# The _init_() Function


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)
print(p1.name)
print(p1.age)


# Object Methods


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()
