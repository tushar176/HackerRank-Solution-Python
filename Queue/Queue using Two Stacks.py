# Enter your code here. Read input from STDIN. Print output to STDOUT
class queueUsingTwoStack:
    def __init__(self):
        #stack1 for enqueue and stack2 is for dequeue
        self.stack1=[]
        self.stack2=[]
        
    def enqueue(self,item):
        self.stack1.append(item)
        #print(self.stack1)
        
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        self.stack2.pop()
    def peek(self):
        if self.stack2!=[]:
            #we have to see the element not pop now
            print(self.stack2[-1])
        else:
            #we have to see the element not pop now
            print(self.stack1[0])

queue=queueUsingTwoStack()
for _ in range(int(input())):
    val = list(map(int,input().split()))
    if val[0] == 1:
        queue.enqueue(val[1])
    elif val[0] == 2:
        queue.dequeue()
    else:
        queue.peek()

