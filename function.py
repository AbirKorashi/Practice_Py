#function defination
def calc_sum(a,b): #function parameter
    return a+b

sum = calc_sum(5,10) #funcyion call argument
print(sum)

def print_hello():
    print("hello")

output = print_hello()
print(output) #none

def avg(a,b,c):
    avrg =( a+b+c) / 3
    print(avrg)
    return avrg

avg(5,12,14)

def displayy_invoice(username,amount,due_date):
    print(f"hello Mr {username}")
    print(f"your bill of {amount} is due: {due_date}")

displayy_invoice("Korashiabir",43.50,"01-10")

# default argument =  A default value for certain parameter s
#                     default is udsed when the argument is omitted
#                  make your function more flexible, reduces # of arguments
#                  1. positional , 2.Default 3.keyword 4. arbitrary

def net_price(list_price,discount=0,tax=0.05):
    return list_price * (1-discount) * (1+tax)

#print(net_price(500,0.10,0.05))
print(net_price(500,0.1))
print(net_price(500,0.1,0))


