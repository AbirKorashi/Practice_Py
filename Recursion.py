#Recursion = a function that call itself from within helps to visualize
#             a complex problem into basic steps, which can be  solved more
#             easily iterively or recuesively

# iterative
def walk(steps):
     for step in range(1,steps+1):
         print(f"you take step #{step}")

walk(100)

#Recursive

def walk(steps):
    if steps == 0:
        return
        walk(steps-1)
        print(f"you take step #{steps}")

walk(100)
# factorial:
def factorial(x):
    if x==1:
        return
    else:
        return x * factorial(x-1)

print(factorial(10))