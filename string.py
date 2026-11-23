name = input("Enter your name : ")
result = len(name)
result2 =name.find(" ")
result3 = name.rfind("S")
name = name.capitalize()
name2 = name.upper()

man= name.isdigit()
print(result)
print(result2)
print(result3)
print(name)
print(name2)
print(man)

phone_number = "012-2839-373-773"
print(phone_number.count("-"))
print(phone_number.replace("-","**"))