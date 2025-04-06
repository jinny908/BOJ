# 9012
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    vps = input().rstrip()
    stack = []
    VPS = True
    for ps in vps:
        if ps == '(':
            stack.append(ps)
        elif ps == ')':
            if stack:
                stack.pop()
            else:
                VPS = False
                break
    if VPS and not stack:
        print("YES")
    else:
        print("NO")