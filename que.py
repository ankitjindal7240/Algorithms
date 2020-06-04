# QUEUE -

queue = [1,2,3,4,5]

def Enqueue(elements):
    queue.append(elements)
Enqueue(6)
print(queue)

def Dequeue(queue):
    if len(queue)>0:
        queue=queue[:len(queue)-1]
        print(queue)
    else :print("Empty")
Dequeue(queue)


def display():
        print(queue[:])
display()