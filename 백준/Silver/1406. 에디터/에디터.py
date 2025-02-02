import sys
from inspect import stack

input = sys.stdin.readline

stack_l = list(input().rstrip())
stack_r = []

n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == 'L':
        if stack_l:
            stack_r.append(stack_l.pop())
    elif command[0] == 'D':
        if stack_r:
            stack_l.append(stack_r.pop())
    elif command[0] == 'B':
        if stack_l:
            stack_l.pop()
    elif command[0] == 'P':
        stack_l.append(command[1])

print(''.join(stack_l + list(reversed(stack_r))))

