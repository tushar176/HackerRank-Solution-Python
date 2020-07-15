#we will be doing this pblm by using two stacks 
n=int(input())
stack=[]
#last index of this list will contain the max item
max_items=[]
max_items.append(float('-inf'))
for i in range(n):
    query = input().split()
    if query[0] == "1":
        x = int(query[1])
        stack.append(x)
        #contain the last element of max_items i.e max element so far
        max_so_far=max_items[-1] 
        if x >= max_so_far:
            max_items.append(x)
        else:
            max_items.append(max_so_far)
    elif query[0] == "2":
        x = stack.pop()
        max_items.pop()
    else: # query[0] == "3"
        print(max_items[-1])