num= int(input("enter the number"))
def palindrome(n):
    if n==1 :
        return 1
    else:
        for i in range(2, n + 1):
            a = ""
            for j in range(i):
                a = a + str(j + 1)
                b = a+ a[len(a) - 2::-1]
        return b
def pyramid(n):
    for i in range(1,num+1):
        print((num-i )*" ",palindrome(i))
pyramid(num)


