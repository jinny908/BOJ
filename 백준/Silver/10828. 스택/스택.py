import sys

input = sys.stdin.readline

n = int(input())

stack = [] 
# 파이썬은 스택 구조를 제공하지 않기에 기본 클래스 list를 이용하여 stack을 표현하기

for i in range(n):
    command = input().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])