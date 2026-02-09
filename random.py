
'''
a = input("Enter Your Name")
print("your name is", a)

b = int(input("Enter your 1st number: "))
c = int(input("Enter your 2nd Number: "))
ans1 = (b + c)
print ("the addition of the given number is: ",ans1) 
ans2 = (b - c)
print ("the subtraction of the given number is: ", ans2)
ans3 = (b * c)
print ("the multiplication of the given number is: ", ans3)
ans4 = (b /c) 
print("the division of the number is: ", ans4)
ans5 = (b % c)
print("the modules of the number is: ", ans5)


name = "Uzair"
for character in name:
    print (character)'''

'''name = "uzair"
len1 = len(name)
print ("the length of your name is", len1)'''
'''

name = "harry harry are you here? I am good"
print(name[-4:-2])'''
'''
a = "UZair is goood boyyy 17777 !!!"
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Uzair" , "harry"))
print(a.islower())
print(a.isupper())
print(a.isprintable())
print(a.isspace())
print(a.swapcase())
print(a.title())


b = int(input("Enter Your age: "))

print("Your age is", b)

if(b > 18):
    print("You are good to drive...!")
else:
    print("You are not allowed...")
'''
'''
age = int(input("Enter your age: "))
if (age < 0):
    print("the age is invalid")
elif( age > 0):
    if(age <= 12):
        print("child")
    elif(age > 12 and age <= 19):
        print("Teenager")
    elif(age > 19 and age <=59):
        print("Adult")
    else:
        print("senior citizen")
else:
    print("age is zero")


'''
'''
import time

hour = int(time.strftime('%H'))

if(hour < 12):
    print("Good moring sir")
elif(hour < 17):
    print("Good after noon sir")
else:
    print("Good evening sir")
    '''
'''
x = int(input("enter the value of x: "))

match x:
    case _ if  x < 0:
        print ("Negative")
    case 0:
        print("Zero")
    case _ if x % 2 == 0:
        print("Even number")
    case _ if x % 2 == 1:
        print("Odd number")
    case _:
        print(x) '''
'''

a = int(input("Enter 1st value: "))
b = int(input("Enter 2nd value: "))

ans1 = (a + b)
print("The addidtion of the given number is: ", ans1)


ans2 = (a - b)
print("The subtraction of the given number is: ", ans2)


ans3 = (a * b)
print("The multiplication of the given number is: ", ans3)


ans4 = (a / b)
print("The divion of the given number is: ", ans4)

'''
'''
type = int(input("Ente rnumber to find its even or odd: "))

match type:
    case _:
        if type % 2 == 0:
            print("The number is even")
        else:
            print("The number is Odd")

'''
'''
for k in range(0 , 5, 6):
    print(k)
    '''
'''
count = 5
while (count > 0):
    print(count)
    count = count - 1
print("Out of the loop")
'''

'''
for i in range(1 , 19):
    print ("5 X", i , "=", 5 * i)
    if(i == 10):
        continue
print("Loop ka khel katm")
    
'''
'''
def calculateGmean(a , b):
    mean = (a * b) / (a + b)
    print(mean)
a = 9
b = 10

calculateGmean( a, b)
c = 19 
d = 42
calculateGmean( c, d)

def whoisGreater(a, b):
    if (a > b):
        print("First number is greater")
    else:
        print("2nd number is greater")

whoisGreater(a, b)

whoisGreater(c, d)
'''
'''
def name(fname, mname, lname = "Shaikh"):
    print("Hello," , fname, mname, lname)
name("Uzair", "Mohsin")
'''
'''
def name (*name):
    print("Hello, ", name[0], name[1], name[2])
name("James", "Buch", "Bar")
'''
'''
def name (**name):
    print("Hello,",name["fname"],name["mname"],name["lname"])
name(mname = "Bruce", lname = "Heill", fname = "Marry")
'''
'''
lst = [1, 2, 3, 4, 5]
print(lst[2])

lst = [i for i in range(4)]
print(lst[-3])

name = ["milo", "aaesha", "faiza", "ali", "zain", "naeem"]
name_abv_4 = [i for i in name if (len(i)> 4)]
print(name_abv_4)
'''

# colors = ["Green","Yellow","Red","Blue","Pupule"]
# colors.sort()
# print(colors)

# num = [9,7,6,8,5,4,3,2,1]
# num.sort()
# print(num)

# list = [1,2,3,4,5,6,7,8,9]
# list.reverse()
# print(list)

# list1 = [5,6,7,3,2,1,8,9,4]
# #list1.sort()
# #list1.reverse()

# print(list1)
# #print(list1.index(3))
# #print(list1.count(3))

# print(list1.insert(2, 786))

# ext1 = ["this", "that", "those"]
# ext2 = ["they", "them","thanos"]
# # ext1.extend(ext2)
# # print(ext1 + ext2)
# print(ext1 + ext2)

#Tuples...
# inti = (1,2,3,4,5)
# print(type(inti), inti)

# countries = ("Russia","America","UAE","India","Newziland")
# temp = list(countries)
# temp.append("Indonesia")
# temp.pop(2)
# temp[2] = "Finland"
# countries = tuple(temp)
# # print(countries)
# countries = ("Russia","America","Russia","UAE","India","Russia","Newziland","Russia")
# res = countries.count("Russia")
# print(res)


# import time

# t = time.strftime("%H:%M:%S")
# hour = int(time.strftime("%H"))
# hour = int(input("Enter your number: "))
# print(hour)
# if (hour > 0 and hour <=12):
#     print("Good Moring Chicha")
# elif (hour > 12 and hour <= 17 ):
#     print("Good Afternoon Chicha")
# if (hour>17 and hour <21):
#     print("Good evening Chicha")
# else:
#     print("Good night chicha")
# print(t)
'''
hi = "my name is {} and i am from {}" 
country = "India"
name = "Uzair"
print(hi.format( name, country))
'''

# country = "India"
# name = "Uzair"

# hello = (f"Hey my name is {name} and i am from {country}")
# print(hello)

# txt = "the prive is only {price:.2f} doolars!"
# print(txt.format(price = 49.96732))

# def square(n):
#     '''Takes in a number n, returns the square of n'''
#     return n**2

# print(square.__doc__)

# def fibbonacci(n):
#     if (n == 1 or n == 0):
#         return n
#     else:
#         return fibbonacci(n -1) + fibbonacci(n - 2)
# print(fibbonacci(6)) 

# s = {9,1,4,7,2,3,4,5,7,8,5,8,6}
# print(type(s))

# info = {"Uzair", 19, 5.11, False, "Male"}
# for i in info:
#     print(i)

# n1 = {1,2,4,8,9}
# n2 = {1,3,5,6,8}
# n1.remove(8)
# print(n1)

# cities = {"Tokyo", "delhi"}
# del cities
# print(cities)

# users = ["admin", "guest", "guest", "user"]
# for u in users:
#     if u == "guest":
#         users.remove(u)
# print(users)

# info = {"name": "Uzair", "age" : 20, "eligible" : True}
# # print(info.keys())
# # print(info.values())
# print(info.items())
# for key, value in info.items():
#     print(f"The information of the following student's key {key} is {value}")

# ep1 = {"name":"Uzair", "Age":20, "education":"Btech", "hobby":"coding"}
# ep2 = {"Work":"Student", "game":"Kbc"}

# # ep1.update(ep2)
# # print(ep1)
# # ep1.pop("name")
# # print(ep1)
# # ep1.clear()
# # print(ep1)
# # ep1.popitem()
# # print(ep1)

# del ep1 ["name"]
# print(ep1)

# for i in range(6):
#     print(i)
#     if i == 4:
#         break
# else:
#     print("sorry no i")

# a = int(input("Enter number: "))
# print(f"the multiplications of {a} is: ")
# for i in range(1,11):
#     print(f"{int(a)} X {i} = {int(a)*i}")

# try:
#     num = int(input("Enter an integer: "))
#     a = [6 , 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer")
# except IndexError:
#     print("index not valid") 
# finally:
#     print("I am always exicuted")

# def func1():
#     try:
#         a = int(input("Enter your 1st number: "))
#         b = int(input("Enter your 2nd number: "))
#         print(a / b)

#     except ZeroDivisionError:
#         print("Cannot divide by zero")

#     except ValueError:
#         print("Invalid input (must be integer)")

#     finally:
#         print("Program finished")

# func1()

# #this is the new life
# a = str(input("enter any value btwn 2 to 6: "))
# if (a == "quit"):
#     print("the value is correct" )
# elif int(a) < 2 and int(a) > 6:
#     raise ValueError("Value should be in between 2 and 6")


# user_input = input("Enter number between 5 and 9 (or type 'Quite' to exit):")
# if user_input.lower() == "quite":
#     print(f"You type {user_input}.So you are quite ")
# else:
#     try:
#         num = int(user_input)
#         if num > 9 or num < 5:
#             raise ValueError("Value should be between 5 and 9")
#         else:
#             print(f"You entered {num}")
#     except Exception as e:
#         print("Error:",e)


# a = 330
# b = 420
# print("A") if a > b else print ("=") if a == b else print("B")

# fruits = ["mango","banana","apple"]
# for index, fruit in enumerate(fruits, start =1):
#     print(index, fruit)



# import uzair
# uzair.uzair()

# x = 10   #global variable
# def func1():
#     x = 11  #local variable
#     print(f"the local variable is {x}")
# func1()
# print(x)


# x = 10   #global variable
# def func1():
#     global x   
#     x = 11
#     print(f"the local variable is {x}")
# func1()

# with open('myfiles.txt','w') as f:
#     f.seek(10)

#     current_position = f.tell()
#     data = f.read(9)
#     print(data) 
#     print(current_position)


# with open ('myfiles.txt','w') as f:
#     f.write("Hello, World I am Uzair Shaikh")
#     f.truncate(12)
# with open('myfiles.txt', 'r') as f:
#     print(f.read())


# mul = lambda x: x * 2
# cube = lambda x: x * x * x
# print(mul(2))
# print(cube(2))

# def is_even(n):
#     return n % 2 == 0

# numbers = [1, 5, 8, 10, 13, 14]

# # filter(condition_function, list)
# result = map(is_even, numbers)

# # Convert the filter object to a list to see the results
# print(list(result)) # Output: [8, 10, 14]


# def square(n):
#     return n**2

# numbers = [1, 2, 3, 4]

# # map(function, list)
# result = map(square, numbers)

# # map returns an iterator, so we convert it to a list to see the results
# print(list(result)) # Output: [1, 4, 9, 16]

# l = [1,3,5,6,8,2,9]
# def grater(x):
#     return x > 4
# newl = list(map(grater, l))
# print(newl)


# a = [1,2,3]
# b = [1,2,3]

# print(a is b)
# print(a == b)

# def hello():
#     print("Hello")
# hello()

# class Details:
#     name = "Uzair"
#     age = 19
# obj1 = Details()
# print(obj1.name)
# print(obj1.age)

# class Details:
#     name = "Rohan"
#     age = 21
#     def sec(self):
#         print("My name is",self.name, "and I am", self.age, "years old")
# obj2 = Details()
# obj2.sec()


# class Person:
#     def __init__(self, n, o):
#         self.name = n
#         self.occ = o
#     def info(self):
#         print(f"{self.name} is a {self.occ}")
# a = Person("Uzair","Data Scientist")
# b = Person("Faiz","Doctor")
# c = Person("Harry", "Devloper")
# d = Person(1,2,3)
# a.info()
# b.info()
# c.info()

# class Details:
#     def __init__(self, animal, group):
#         self.animal = animal
#         self.group = group

# obj1 = Details("Crab", "Crustaceans")
# print(obj1.animal, "belongs to the", obj1.group, "group.")


# def my_decorator(func):
#     def wrapper():
#         print("Good Morning...! Hope u feeling good today...")
#         func()
#         print("We will catch you later...good by")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

# def my_logger(func):
#     def wrapper():
#         print("Function is called")
#         func()
#     return wrapper

# @my_logger
# def say_hello():
#     print("Hello")
# say_hello()

# class Myclass:
#     def __init__(self, value):
#         self.og_value = value
#     @property
#     def value(self):
#         return self.og_value
    

#     @value.setter
#     def value (self, new_value):
#         self.og_value = new_value
        
# obj = Myclass(10)
# obj.value = 100
# print(obj.value)

# class Parent():
#     def func1(self):
#         print("This function is in parent class.")
# class Child(Parent):
#     def func2(self):
#         print("This function is in child class.")
# object = Child()
# object.func1()
# object.func2()

# multiple inheritance
# class mother:
#     mothername = ""
#     def mother(self):
#         print(self.mother)
# class father:
#     fathername = ""
#     def father(self):
#         print(self.father)
# class son(mother,father):
#     def parent(self):
#         print("Father's name is:", self.father)
#         print("Mother's name is:", self.mother)
# s1 = son()
# s1.father = "DAD"
# s1.mother = "Mommy"
# s1.parent()

# class School:
#     def __init__(self):
#         self.__uzair = 10000
#     def show(self):
#         print(self.__uzair)
# obj = School()
# obj.show()

# class Account(School):
#     def __init__(self):
#         self.__balance = 1000   # private variable

#     def show(self):
#         print(self.__balance)
# a = Account()
# a.show()


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return(f"The name of the student is {self.name}. And he is {self.age}.")

# a = Student("Uzair",20)
# print(a)

# class Adult:
#     @staticmethod
#     def is_adult(age):
#         return age >= 18
# # print(Adult.is_adult(20))


# class MyClass:
#     class_variable = 0
    
#     def __init__(self):
#         MyClass.class_variable += 1
        
#     def print_class_variable(self):
#         print(MyClass.class_variable)
        

# obj1 = MyClass()
# # obj2 = MyClass()

# obj1.print_class_variable()
# obj2.print_class_variable()

# class MyClass:
#     def __init__(self, name):
#         self.name = name
        
#     def print_name(self):
#         print(self.name)

# obj1 = MyClass("John")
# obj2 = MyClass("Jane")

# obj1.print_name()
# obj2.print_name()

#Cluttering Files

# import os
# def clutter():
#   path = input("enter the path : ")
#   f = input("enter the format .png or .jpg or.pdf ")
#   l = 0
#   for i in os.listdir(path):
#       os.rename(f'{path}{i}',f"{path}{l}.{f}")
#       l = l + 1
  
# clutter()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     @classmethod
#     def form_string(cls, string):
#         name, age = string.split(',')
#         return cls(name,int(age))
# person = Person.form_string("John Doe, 30")
# print(person.name,person.age)



# #super keyword
# class emplyee():
#     def __init__(self , name, id):
#         self.name = name
#         self.id = id
# class Programmer(emplyee):
#     def __init__(self, name, id, lang):
#         super().__init__(name, id)
#         self.lang = lang
# harry = emplyee("Harry","122")
# uzair = Programmer("Uzair","786","python")
# print(uzair.name)
# print(uzair.id)
# print(uzair.lang)

# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method.")

# class ChildClass(ParentClass):
#     def child_method(self):
#         print("This is the child method.")
#         super().parent_method()
# child_object = ParentClass()
# child_object.parent_method

# from uzair import Employee

# e = Employee("Uzair", "20")
# print(e)

# class Shape:
#     def area(self):
#         print("Area calculating")
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         print("Calculating are of a circle")
#         super().area()
#         return 3.14 * self.radius * self.radius
# cir = Circle(5)
# print(cir.area())

# class Addition:
#     def __init__(self, x , y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return (self.x + other.x + self.y + other.y)

# add1 = Addition(4,5)
# add2 = Addition(6,7)
# add3 = add1 + add2
# print(add3)


# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#     def sound_made(self):
#         print("Sound made by animal is...")
        
# class mammal:
#     def __init__(self,name,fur_color):
#         self.name = name
#         self.fur_color = fur_color
# class cat:
#     def __init__(self, name, breed, fur_color):
#         Animal.__init__(self, name, species="cat")
#         mammal.__init__(self, name,fur_color)
#         self.breed = breed
#     def sound_made(self):
#         print("Miyannuuuunnnnn")
# o = cat("Billu","persian","white")
# print(o.name)
# print(o.fur_color)
# print(o.breed)



# class Animal:
#     def __init__(self,name,species):
#         self.name = name
#         self.species = species
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Species: {self.species}")
# class dog(Animal):
#     def __init__(self,name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
#     def show_details(self):
#         Animal.show_details(self)
#         print(f"Breed: {self.breed}")
# class GermanShepard:
#     def __init__(self,name,color):
#         dog.__init__(self, name, breed ="German Shepard")
#         self.color = color
#     def show_details(self):
#         dog.show_details(self)
#         print(f"Color: {self.color}")
# o = GermanShepard("Dogesh Bhau","golden")
# o.show_details()

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show_details(self):
#         print("Name: ",self.name)
#         print("Age: ",self.age)
# class Person(Human):
#     def __init__(self, name, age, address):
#         Human.__init__(self, name, age)
#         self.address = address
#     def show_details(self):
#         print("Address: ",self.address)
# class Program:
#     def __init__(self,program_name,duration):
#         self.program_name = program_name
#         self.duration = duration
#     def show_details(self):
#         print("Program Name: ",self.program_name)
#         print("Duration: ",self.duration)
# class Student(Person):
#     def __init__(self,name, age, address, Program):
#         Person.__init__(self,name,age,address)
#         self.program = Program
#     def show_details(self):
#         Person.show_details(self)
#         self.program.show_details()
# program = Program("Computer Science", 4)
# student = Student("John Doe", 25, "123 Main St.", program)
# student.show_details()



# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def show_details(self):
#         print("Name:", self.name)

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name)
#         self.breed = breed

#     def show_details(self):
#         Animal.show_details(self)
#         print("Species: Dog")
#         print("Breed:", self.breed)

# class Cat(Animal):
#     def __init__(self, name, color):
#         Animal.__init__(self, name)
#         self.color = color

#     def show_details(self):
#         Animal.show_details(self)
#         print("Species: Cat")
#         print("Color:", self.color)


# dog = Dog("Max", "Golden Retriever")
# dog.show_details()
# cat = Cat("Luna", "Black")
# cat.show_details()


from os import system

names = ["AayushGarg15", "Yuniek", "NiteshUpadhyay2"]

for name in names:
    system(
        f'powershell -Command "Add-Type -AssemblyName System.Speech; '
        f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Shoutout to {name}\')"'
    )

