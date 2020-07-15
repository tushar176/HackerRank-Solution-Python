
import os
import re
import sys

# Complete the isBalanced function below.
def is_match(p1, p2):
    if (p1 == "(" and p2 == ")") or (p1 == "{" and p2 == "}") or (p1 == "[" and p2 == "]") :
        return True
    else:
        return False


def isBalanced(paren_string):
    s=[]
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.append(paren)
        else:
            if s==[]:
                is_balanced = False
            else:
                if not is_match(s.pop(), paren):
                    is_balanced = False
        index += 1

    if s==[] and is_balanced:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
