# if you have to print whole sequence
def look_and_say_sequence(n):
    a=["1"]
    for i in range(2,n+1):
        counter=0
        k=0
        string = ""

        for j in range( len(str(a[i-2]))):
            number=a[i-2][k]
            if a[i-2][j] ==a[i-2][k]:
                counter=counter+1
                if j==len(str(a[i-2]))-1:
                    string = string + str(counter) + str(number)
                    k = counter
                    counter = 1

            else:
                string=string+ str(counter) + str(number)
                k = k+ counter
                counter=1
                if j == len(str(a[i - 2])) - 1:
                    string = string + str(1) +str(a[i-2][j])
                    k = counter
                    counter = 1
        a.append(string)
    print(a)
look_and_say_sequence(8)




#if you have to print only nth term
def look_and_say_sequence(n):
    a=["1"]
    for i in range(2,n+1):
        counter=0
        k=0
        string = ""

        for j in range( len(str(a[0]))):
            number=a[0][k]
            if a[0][j] ==a[0][k]:
                counter=counter+1
                if j==len(str(a[0]))-1:
                    string = string + str(counter) + str(number)
                    k = counter
                    counter = 1

            else:
                string=string+ str(counter) + str(number)
                k = k+ counter
                counter=1
                if j == len(str(a[0])) - 1:
                    string = string + str(1) +str(a[0][j])
                    k = counter
                    counter = 1
        a[0]=string
    print(a)
look_and_say_sequence(5)