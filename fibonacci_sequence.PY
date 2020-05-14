number= int(input("enter the no."))
#1. recursive approach

def Fibonacci(n):
    """fibbonaci no. 0 1 1 2 3 5 8 13 21......"""
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
print("sequence using recursive approach")
for i in range(1,number+1):
       print(Fibonacci(i))
"""results:
for number = 1 : 0
for number =  2:0 1 
for number =  3: 0 1 1
for number = 8 : 0 1 1 2 3 5 8 13
"""




#2. iterative approach


def fibonacci_2(n):
    first_term = 0
    second_term = 1
    for i in range(0,number):
        print(first_term)
        next_term = first_term+second_term
        first_term = second_term
        second_term = next_term
        i =i+1
print("sequence using iterative approach")
fibonacci_2(number)

"""results:
for number = 1 : 0
for number = 2:0 1 
for number = 3: 0 1 1
for number = 6 : 0 1 1 2 3 5 8 
"""
