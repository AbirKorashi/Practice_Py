import time

# my_time = int(input("Enter the time in second :"))
#
# for x in range (0,my_time):
#     print(x)
#     time.sleep(1)
#
# print("Times up!")

#Reverse CountDown
# my_time = int(input("Enter the time in second :"))
#
# for x in range (my_time,0,-1):
#     print(x)
#     time.sleep(1)
#
# print("Times up!")

# Digital clock

my_time = int(input("Enter the time in second :"))

for x in range (my_time,0,-1):
    second = x% 60
    minute = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours:02}:{minute:02}:{second:02}")
    time.sleep(1)

print("Times up!")