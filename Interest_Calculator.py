# While lop = execute some code whilw some condition remains true

# name = input("Enter your name :")
#
# while name == "":
#     print("you didn not enter your name ")
#     #name = input("Enter your name :")
#
# print(f"Hello {name}")

# age = int(input("Enter your age :"))
#
# while age< 0 :
#     print("Age cant be negetive")
#     age = input("Enter your age :")
#
# print(f"you are {age} years old")


#Intereset Calculator

principal = 0
rate = 0
time =0

while principal <= 0 :
    principal = float(input("Enter the principal ammount: "))
    if principal <= 0:
        print("PRINCIPAL can't be or less than equal ")
    
while rate <= 0 :
      rate = float(input("Enter the Interest rate: "))
      if rate <= 0:
             print("Interest rate can't be or less than equal ")

while time <= 0 :
    time = int(input("Enter the time: "))
    if time <= 0:
        print("time can't be or less than equal ")

rate = rate/100
Future_value = (principal * (1+rate)**time)

print(Future_value)


for x in range(1,11):
    print(x)

for x in reversed(range(1,11)):
    print(x)
