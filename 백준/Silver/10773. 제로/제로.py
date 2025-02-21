import sys

input = sys.stdin.readline
stack = []

n = int(input())

for i in range(n):
    call = int(input())
    if call == 0:
        stack.pop()
    else:
        stack.append(call)

print(sum(stack))



