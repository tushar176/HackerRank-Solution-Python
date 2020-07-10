
if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    D = int(nd[1])

    A = list(map(int, input().rstrip().split()))

    for i in range(D):
        a=A.pop(0)
        A.append(a)

    for i in A:       
        print(i,end=" ") 


######## gfg array rotation in place

# def rotateArr(A,D,N):
#     #Your code here
#     for i in range(math.gcd(N,D)):
#         temp=A[i]
#         j=i
#         while 1:
#             k=(j+D)%N
#             if(k==i):
#                 break
#             A[j]=A[k]
#             j=k   
#         A[j]=temp
