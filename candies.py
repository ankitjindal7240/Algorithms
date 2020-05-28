def candy_distribution(total_candies,n):

    number_of_person = n
    diff =1                                         #tereating as AP
    a = 1                                           #first term of AP
    sum= n * (1 + n) * 0.5                          #sum of n integers
    i=1                                             #first round
    while (total_candies-sum)>0:
       sum = i*(n) ** 2 + sum + n * (1 + n) * 0.5   #sum = jitne round ho chuke hai*n^2 +n integers ka sum +phele jo sum ho chuka hai
       i = i+1
    remaining_candies = total_candies - sum +  (i-1)*(n) ** 2 + n * (1 + n) * 0.5 #abhi jo sum hai usse phele wala sum minus kiya hai
    if remaining_candies==0:
        answer=[]
        for j in range(1, n + 1):
            term= 1 + (j-1) + (i-1) * n             #agle bande ko jo candies milne wali hai =a+(n-1)d  + jitne round ho chuke hai*n
            answer.append(term)
        print(answer)
    elif remaining_candies<0:                       #iska matalb hai phele he round me candies puri ho gai
        remaining_candies= remaining_candies + sum  #- ((i-1) * n) ** 2 - n * (1 + n) * 0.5
        answer = []
        for k in range(1, n + 1):
            term = 1 +  (k - 1)                     #agle ko jitni candies milne wali hai
            remaining_candies = remaining_candies - term
            if remaining_candies > 0:
                answer.append(term)
            else:                                      #agle ko jitni candies milne wali hai vo agr bachi hui candies se jyada hai
                answer.append((remaining_candies + term))
                answer = answer + [0] * (n - k)         #jo bachi hai use de do
                print(answer)
                break
    else:
        answer=[]
        for k in range(1, n + 1):
            term = 1 + (i-1) * n + (k - 1)
            remaining_candies = remaining_candies-term
            if remaining_candies>0:
                answer.append(term)
            else:
                answer.append((remaining_candies+term))
                answer = answer + [0]*(n - k)
                break
        print(answer)

candies=[7,10,21,100,101,16,108,200,210,20101,20000,20001]
for i in range(len(candies)):
    #let no of people 5
    candy_distribution(candies[i],5)