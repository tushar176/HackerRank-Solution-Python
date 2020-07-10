###############  METHOD-1 ######################
# def arrayManipulation(n, queries):
#     lst=[0]*n
#     for l in queries:

#         for i in range(l[0]-1,l[1]):
#             lst[i]+=l[2]
#     return max(lst)

################## METHOD-2 #######################

def arrayManipulation(n, queries):
    lst=[0]*(n+1)

    for l in queries:
        lst[l[0] - 1] += l[2]
        if l[1] != len(lst):
            lst[l[1]] -= l[2]

    maxval=temp=0
    for q in lst:
        temp += q
        if temp > maxval:
            maxval = temp
    return maxval