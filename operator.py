# a = 2
# if a > 1 and a <= 10: # yes
#     print('1 < a <= 10')
# if a == 2 or a >= 1: # yes
#     print('a is greater than or equal to 1')
# if a == 2: # yes
#     print('a is 2')
# if a != 2: # no
#     print('a is not 2')
#
# if a is 2: # yes
#     print('a is 2')
# if a is not 4: # yes
   # print('a is not 4')


for x in range(1,11):
    print(x)

for x in reversed(range(1,11)):
    print(x)

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

for x in range(1,21):
    if x==13:
        #continue
        break
    else:
        print(x)


#NESTED LOOP


for x in range(3):
    for y in range(1, 10):
         print(y, end=" ")
    print()


rows = int(input("Enter the * of rows :"))
columns = int(input("Enter the * of columns :"))
symbol = input("Enter a symbol to use :")

for x in range(rows):
    for y in range(columns):
         print(symbol, end=" ")
    print()



