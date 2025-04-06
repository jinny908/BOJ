import sys
input = sys.stdin.readline

arr = input().strip()
stack = []

for char in arr:
    if char == '(' or char == '[':
        stack.append(char)
    elif char == ')':
        temp = 0
        found = False
        while stack:
            top = stack.pop()
            if top == '(':
                stack.append(2 if temp == 0 else 2 * temp)
                found = True
                break
            elif isinstance(top, int):
                temp += top
            else:
                print(0)
                sys.exit()
        if not found:
            print(0)
            sys.exit()
    elif char == ']':
        temp = 0
        found = False
        while stack:
            top = stack.pop()
            if top == '[':
                stack.append(3 if temp == 0 else 3 * temp)
                found = True
                break
            elif isinstance(top, int):
                temp += top
            else:
                print(0)
                sys.exit()
        if not found:
            print(0)
            sys.exit()
    else:
        print(0)
        sys.exit()

result = 0
for num in stack:
    if isinstance(num, int):
        result += num
    else:
        print(0)
        sys.exit()

print(result)