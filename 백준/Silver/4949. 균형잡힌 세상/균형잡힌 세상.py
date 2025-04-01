import sys

input = sys.stdin.readline

while True:
    word = input().rstrip()
    stack = []

    if word =='.':
        break

    for char in word:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
                break
        elif char == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(char)
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')