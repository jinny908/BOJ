# test case
# 2
# <<BP<A>>Cd-
# ThIsIsS3Cr3t

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    pwd = input().rstrip()
    stack_l = []
    stack_r = []
    for i in pwd:
        if i == '-':
            if stack_l:
                stack_l.pop()
        elif i == '<':
            if stack_l:
                stack_r.append(stack_l.pop())
        elif i == '>':
            if stack_r:
                stack_l.append(stack_r.pop())
        else:
            stack_l.append(i)

    print(''.join(stack_l + list(reversed(stack_r))))


