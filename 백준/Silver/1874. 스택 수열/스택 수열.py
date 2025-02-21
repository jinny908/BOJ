import sys
input = sys.stdin.readline

stack = []
temp = 1
ans = []
available = True

n = int(input())

for i in range(n):
    num = int(input())
    while temp <= num:
        stack.append(temp)
        temp += 1
        ans.append('+')
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        available = False
        break

if available == False:
    print('NO')
else:
    for i in ans:
        print(i)