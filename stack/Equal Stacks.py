#!/bin/python3

import os
import sys
# def is_empty(stack):
#     if stack==[]:
#         return True
#     else:
#         return False

def equalStacks(h1, h2, h3):
    lst1=[]
    lst2=[]
    lst3=[]
    temp1=temp2=temp3=0
    for i in range(len(h1)-1,-1,-1):
        temp1+=h1[i]
        lst1.append(temp1)

    for j in range(len(h2)-1,-1,-1):
        temp2+=h2[j]
        lst2.append(temp2)

    for k in range(len(h3)-1,-1,-1):
        temp3+=h3[k]
        lst3.append(temp3)

    while True:
        if lst1==[] or lst2==[] or lst3==[]:
            return 0
        top1=lst1[-1]
        top2=lst2[-1]
        top3=lst3[-1]

        if top1==top2 and top2==top3:
            return top1

        elif top1>=top2 and top1>=top3:
            lst1.pop()
        elif top2>=top1 and top2>=top3:
            lst2.pop()
        elif top3>=top1 and top3>=top2:
            lst3.pop()        

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
