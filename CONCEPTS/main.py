# 1ST PYTHON PROGRAM
print("Hello world!!")
print("This is Akash Halder & This is my python based revision notes\n")
# 2ND PROGRAM => TAKING INPUT FROM USER
name = input("Enter your Name: ")
print("Hi!", name)

# ================================================== 1. COMMENTS ✅============================================
# Single line comment
'''MULTILINE
COMMENT => THNGS WRITTEN IN COMMENTS WILL BE IGNORED BY THE INTERPRETER'''

# ==================================================== 2. VARIABLES IN PYTHON ✅ =================================
a = 69
print(a,"This is an integer data type \n")
b = 99.99
print(b,"This is a floating point data type \n")
c = "Akash"
print(c,"This is a String data type \n")
d = True # or False
print(d,"This is a boolean data type \n")
e = None
print(e,"This a None data type \n")

# ================================================= 3. TYPECASTING ✅==============================================
# TYPECASTING MEANS CONVERTING ONE DATATYPE INTO ANOTHER DATAYPE
f = "5" #This is a string datatype
print(int(f)+1)  #the string is typecasted to integer datatype 1st then an addition operator is perfromed

num = int(input("Enter a number: "))
print(num+1)

# ================================================= 4 . OPERATORS ✅================================================
# Arithmetic operators:
num1 = 10
num2 = 3
print("num1 + num2 = ", num1+num2)
print("num1 - num2 = ", num1-num2)
print("num1 * num2 = ", num1*num2)
print("num1 / num2 = ", num1/num2)
print("num1 // num2 = ", num1//num2)
print("num1 ** num2 = ", num1**num2,"\n")

# Assignment operators:
a = 4
a += 2 
a -= 2 
a *= 2 
a /= 2 

# Comparison Operators:
x = 8
y = 64
z =8
print(x>y)
print(x<y)
print(x!=y)
print(x==y,"\n")

# Logical Operators: 
print(x==z and x<y)
print(x==z or x<y)
print(not(True))
print(not(False),"\n")

# ========================================================== 5. STRINGS ✅===================================================

name = 'Akash'
number = "69"
print(name)
# print(name[a:b])  # start from a all the way to b-1
print(name[0:3])  # start from 0 all the way to 2 (3-1)
print(name[1:4])  # start from 1 all the way to 3(4-1)

print(name.upper())
print(name.capitalize())
print(name.count("r"))
print(number.isalnum())

a1 = 'Akash'
a2 = "learnt coding from"
a3 = '''Harry'''
print(a1, a2, a3,"\n")

'''a1[0]= "j" '''  # This will throw a ERROR Bcoz <STRINGS R IMMUTABLE>

# ========================================================= 6. LIST & METHODS ✅===============================================
l1 = [3, 5, 7, 69, 99, 100,]

print(type(l1))
print(l1)
# l1.remove("Harry")
print(l1)
print(l1.count(99))
# l1.sort()
# l1.append(99)
# l1.extend([89, 90, 98, 99])

l1[0] = "Akash"  # This line didn't threw error because List r Mutable
print(l1)

# ==================================================== 7. TUPLES & METHODS ✅=======================================================
t = (3, 4, 23, 23, 5)
print(t.count(5))
print(t.index(23))

# t[0]= 89
# The above line will throw an ERROR as tuples are immutable(can't be changed)

# ===================================================== 8. SETS ✅====================================================================
# SETS is a collection of well-defined elements
# R a 11th ka SET THEORY walla chp. ka Programming me practical ha

a1 = {3, 5, 23, 5, 5, 25, 5}
a2 = {3, 5, 23, 7, 8, 9, 69}

# print(a1.pop())
# print(a1)
# print(a2)
print(a1.union(a2),"\n")
print(a1.intersection(a2),"\n")

# ======================================================= 9. DICTIONARY ✅==================================================================
# DIFFERENCE BETWEEN DICTIONARY & SETS:
"""a = {}
b = set()
print(a, type(a))
print(b, type(b))"""
# *************************************
dict1 = {"good": "Something Pleasant", "fetch": "To bring", "1": "The number 1"}
marks = {"Harshit": 69, "Harry": 96, "Akash": 99}

print(dict1["good"])
print(marks["Akash"])

# Dictionary Methods:
marks["Priyanka"] = 34
print(marks)

print(marks.get("Priyanka Chopra"))
# print(marks("Priyanka")) # This will not give error
# print(marks("Priyanka Chopra")) # But This will show ERROR as Priyanka Chopra is not defined in dict.
print(marks.get("Priyanka Chopra")) # This will save you from Error
print(marks.keys())
print(marks.values())
print(marks.items(),"\n")

# ======================================================= 10. IF-ELSE ✅=======================================================================
age = int(input("Enter your age: "))
if(age >= 18):
    print("Yes, you can drive\n")
elif(age == 1, 2, 3, 4, 5, 6, 7, 8, 9):
    print("You are a baby!\n")
elif(age == 10):
    print("Oh! Common Kiddo! You need to be 18+ to get a driving license & drive\n")
else:
    print("No, you can go home\n")

print("End of program")
# SHORT HAND IF ELSE:
A = int(input("Enter a number: "))
B = int(input("Enter another number: "))
print("B A se bada ha bhai\n") if A<B else print("A B se chota hai bhai\n")

# ========================================================= 11. MATCH CASE ✅ ====================================================================
# Write a python program to print a table of number which lies between 1 and 10

table = int(input("Enter the number from 1 to 10: "))

match table:
        case 1:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 2:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 3:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 4:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 5:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 6:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 7:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 8:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 9:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case 10:
            for i in range(1, 11):
                print(f"{table} X {i} = {table*i}")
        case _:
            print('Match not found. Please enter the number between 1 to 10 ')


# ====================================================================== 12. LOOPS ✅ ====================================================

n = input("Enter your name: ")
# FOR LOOP
for i in range (10):
    print("Hi!",n ,"\n")

items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)


# WHILE LOOP
i = 0
while(i<10):
    print(i)
    i += 1
print("The program has finished executing...")

# while(True):
#     print("Hello Everyone")

while(True):
    num = int(input("Enter a number: "))
    print(num)
    if (num==0):
        break

# ============================================================= 13. FUNCTIONS ✅ ============================================================
def greethello(name, ending):
    print("Hello,",name)
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print(ending)

def lettergenerator(name, date):
    st = f"Hi mam, \nThis is{name} and I will not come to school on {date}"
    print(st)

def average(a,b):
     return (a+b)/2

print("This will execute 1st")
greethello("Akash ", "Thank you") # Because greethello is defined & registered as a function
greethello("Shivam ", "Thank you")

lettergenerator(" Akash", "26/07/34")
print("done")

print(average(5, 25))


# ============================================================== 14. EXCEPTIONAL HANDLING ✅ ==================================================
""" a = int(input("Enter your number: "))
print(a+3)
 But if user Enters a string or alphanumeric value it will show Error
& the program will halt.But we don't want that.We want our program to run continuously
Therefore, we use Try & Except METHOD.This will print error but our program
 will run till it is finished """

try:
    num = int(input("Enter your number: "))
    print(num)
except Exception as e:
    print("Opps!!Some Error Occured...", e) 
 
