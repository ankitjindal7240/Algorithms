num= int(input("enter the number"))
def palindrome(n):
    a = int(n*"1")
    b = a*a
    return b
def pyramid(n):
    for i in range(1,num+1):
        print((num-i )*" ",palindrome(i))
pyramid(num)