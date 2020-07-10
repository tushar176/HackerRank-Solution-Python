# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X=int(input())
lst=list(map(int,input().strip().split(" ")))
n=int(input())
dic=Counter(lst)
sum=0
for i in range(n):
    size,rupee=map(int,input().strip().split(" "))
    if (size in dic.keys()) and (dic[size]!=0):
        sum+=rupee
        dic[size]-=1

print(sum)
