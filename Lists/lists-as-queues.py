#queues work in the principle of first-in first-out
#to use lists as queues we use **collections.deque** module

from collections import deque

#create a list as a queue

queue = deque(["kevin","godwin","shernice","njoki"])

#adding/appending an item at the end of the list

queue.append("elvis")
queue.append("Ann")

#printing the first list

print("the first queue is :",queue)

#poping an item from the list
queue.popleft()

#printing the list after poping
print("list after poping: ",queue)
