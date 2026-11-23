# name =input("Enter your name")
# age = int(input("Enter your age"))
# age= age+ 1
#
# print(f"hello {name}")
#
# print(f"you are {age} years old")

# length = int(input("Enter the length of a rectangle: "))
# width = int(input("Enter the width of a rectangle: "))
# height = int(input("Enter the height of a rectangle: "))
#
# volume = length * width * height
#
# print(f"The volume is : {volume} cm^3")
#
# #MATH IN PYTHON
#
# friends = 5
#
# freinds = friends +1
#
#
# print(freinds)


# Making Python Calculator:

operator = input("Enter an operator(+ - * / ) : ")
num1 = float(input("Enter the 1st number"))
num2 = float(input("Enter the 2nd number"))

if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
elif operator == '/':
    result = num1 / num2
    print(result)


# Temperature convertion with python:

unit = input("is the temperature in celcius or Farenheit (C/F): ")
temp = float(input("Enter the temoerature : "))

if unit == 'C':
    temp = (9 * temp / 5 + 32)
    print(f"The temparature in ferenheit is : {temp} F")

elif unit == 'F':
    temp = (temp-32 * (5/9))
    print(f"The temparature in Celcius  is : {temp} c")
else :
    print(f"{unit} is in invalid measurement")
