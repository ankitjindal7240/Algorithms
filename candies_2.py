def candy_distribution(total_candies,n):
    #total_candies = 170
    number_of_persons = n
    diff = 1
    a = 1
    sum = n * (1 + n) * 0.5
    i = 1  # first round
    while (total_candies - sum) > 0:
        sum = i * (n) ** 2 + sum + n * (1 + n) * 0.5
        i = i + 1
    remaining_candies = total_candies - sum + (i - 1) * (n) ** 2 + n * (1 + n) * 0.5
    answer = []
    for j in range(1, n + 1):
        term = i * (2 * j + (i - 1) * n) * 0.5
        previous_term = (i - 1) * (2 * j + (i - 2) * n) * 0.5
        if remaining_candies - term + previous_term > 0:
            answer.append(term)
            remaining_candies = remaining_candies - term + previous_term
        elif remaining_candies - term + previous_term < 0:
            i = i - 1
            term = i * (2 * j + (i - 1) * n) * 0.5
            answer.append(term + remaining_candies)
            remaining_candies = 0
            break
        else:
            answer.append(term)
            remaining_candies = 0
            i = i - 1
            break
    if len(answer) < n:
        for j in range(len(answer) + 1, n + 1):
            term = i * (2 * j + (i - 1) * n) * 0.5
            answer.append(term)
    print(answer)
candies=[7,10,21,100,101,16,108,200,210,20101,20000,20001]
for k in range(len(candies)):
    #let no of people 5
    candy_distribution(candies[k],5)