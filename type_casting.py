
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
user_input = input("Enter number between 5 and 9 (or type 'Quite' to exit):")
if user_input.lower() == "quite":
    print(f"You type {user_input}.So you are quite ")
else:
    try:
        num = int(user_input)
        if num > 9 or num < 5:
            raise ValueError("Value should be between 5 and 9")
        else:
            print(f"You entered {num}")
    except Exception as e:
        print("Error:",e)