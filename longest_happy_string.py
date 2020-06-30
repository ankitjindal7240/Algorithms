arr=[6,5,5]
def happy_string(arr):
    elements=["a","b","c"]
    d=max(arr)
    if arr[0]==arr[1]==arr[2]:
        return (arr[0]*"abc")


    def more_than_1_max(arr):
        i=0
        for j in range(3):
            if arr[j]==d:
                i=i+1
        if i>1:
            return 1
    def more_than_1_min(arr):
        i=0
        for j in range(3):
            if arr[j]==min(arr):
                i=i+1
        if i>1:
            return 1

    if more_than_1_max(arr):
        p=[]
        for i in range(3):
            if arr[i]!=min(arr):
                p.append(elements[i])
        string=min(arr)*"abc"
        string=string+((max(arr)-min(arr))*(p[0]+p[1]))
        return (string)


    temp_arr=arr[:]
    def return_index_of_max(arr):
        for i in range(len(arr)):
            if arr[i]==max(arr):
                return i

    places_must_be_filled=(max(arr)-1)//2
    if places_must_be_filled==0:
        string=arr[0]*elements[0] +arr[1]*elements[1] +arr[2]*elements[2]
        return (string)

    temp_arr.pop(return_index_of_max(arr))
    temp_elements=[]

    max_elememnt=return_index_of_max(arr)
    if max_elememnt!=0:
        temp_elements.insert(0,"a")
    if max_elememnt!=1:
        temp_elements.insert(0,"b")
    if max_elememnt!=2:
        temp_elements.insert(0,"c")
    temp_elements.reverse()
    remaining_element_1=temp_arr[0]
    remaining_element_2=temp_arr[1]
    sum_of_remaining=sum(temp_arr)
    max_element = elements[return_index_of_max(arr)]


    if sum_of_remaining<places_must_be_filled:
        max_element=elements[return_index_of_max(arr)]
        string=2*max_element
        while remaining_element_1:
            string=string+ temp_elements[0] +(2*max_element)
            remaining_element_1=remaining_element_1 - 1
        while remaining_element_2:
            string=string+ temp_elements[1] +(2*max_element)
            remaining_element_2=remaining_element_2 - 1
        return (string)

    else:
        max_element = elements[return_index_of_max(arr)]
        string = 2 * max_element
        if (remaining_element_1 or remaining_element_2 )> places_must_be_filled:
            if (remaining_element_2+remaining_element_1)/2 >places_must_be_filled:
                if (remaining_element_1%2 and remaining_element_2%2) !=0:
                    p=""
                    while remaining_element_1>1 and remaining_element_2>1:
                        p= p+ 2*temp_elements[0] +2*temp_elements[1]
                        remaining_element_2=remaining_element_2-2
                        remaining_element_1=remaining_element_1-2
                    if remaining_element_1 > 1:
                        p=p+ (remaining_element_1*temp_elements[0] ) +temp_elements[1]
                    else:
                        p = p + temp_elements[0] + (remaining_element_2 * temp_elements[1])
                elif remaining_element_1%2!=0:
                    p=""
                    while remaining_element_1 > 1 and remaining_element_2 :
                        p = p + 2 * temp_elements[0] + 2 * temp_elements[1]
                        remaining_element_2 = remaining_element_2 - 2
                        remaining_element_1 = remaining_element_1 - 2
                    if remaining_element_1>1:
                        p=p+ remaining_element_1* temp_elements[0]
                    else:
                        p = p+ temp_elements[0] +remaining_element_2*temp_elements[1]
                elif remaining_element_2%2 !=0:
                    p = ""
                    while remaining_element_2 > 1 and remaining_element_1:
                        p = p + 2 * temp_elements[0] + 2 * temp_elements[1]
                        remaining_element_2 = remaining_element_2 - 2
                        remaining_element_1 = remaining_element_1 - 2
                    if remaining_element_2 > 1:
                        p = p + remaining_element_2 * temp_elements[1]
                    else:
                        p = p  + remaining_element_1 * temp_elements[0]+ temp_elements[1]
                else:
                    p=""
                    while remaining_element_2 and remaining_element_1:
                        p= p+ 2*temp_elements[0] + 2*temp_elements[1]
                        remaining_element_2 = remaining_element_2 - 2
                        remaining_element_1 = remaining_element_1 - 2
                    if remaining_element_1:
                        p= p+remaining_element_1*temp_elements[0]
                    if remaining_element_2:
                        p=p+remaining_element_2*temp_elements[1]
             
                string=p[:(len(p)-(2+ 2*places_must_be_filled))]
                i=(len(p)-(2+ 2*places_must_be_filled))
                while i <len(p)-2:
                    string=string+2*max_element+p[i:i+2]
                    i=i+2
                if max(arr)%2==0:
                    string=string + 2*max_element +p[len(p)-2:]
                else:
                    string=string + max_element +p[len(p)-2:]

                return string
            else:
                p = remaining_element_1 * temp_elements[0] + remaining_element_2 * temp_elements[1]
                no_of_pairs_to_be_formed = sum_of_remaining - places_must_be_filled
                i = 0
                while i < (2 * no_of_pairs_to_be_formed):
                    string = string + p[i:i + 2] + (2 * max_element)
                    i = i + 2
                for i in range(2 * no_of_pairs_to_be_formed, len(p)):
                    string = string + p[i] + (2 * max_element)
                if max(arr) % 2 != 0:
                    string = string[:len(string) - 1]
                return (string)

        else:
            p=remaining_element_1*temp_elements[0] + remaining_element_2*temp_elements[1]
            no_of_pairs_to_be_formed=sum_of_remaining-places_must_be_filled
            i=0
            while i< (2*no_of_pairs_to_be_formed):
                string=string +p[i:i+2]  +(2*max_element)
                i=i+2
            for i in range(2*no_of_pairs_to_be_formed,len(p)):
                string = string + p[i] + (2 * max_element)
            if max(arr)%2 !=0:
                string=string[:len(string)-1]
            return (string)

arrs=[[0,0,0],[1,1,1],[7,1,1],[7,7,1],[5,4,4],[10,10,9],[11,9,9],[7,8,9],[9,2,3],[9,2,1]]
for arr in arrs:
        print(happy_string(arr))


