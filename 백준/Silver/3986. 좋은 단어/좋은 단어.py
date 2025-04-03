import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
for _ in range(n):
    word = list(input().strip())
    stack = []
    for ch in word:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    if not stack: # 최종적으로 스택이 비어있으면 좋은 단어이다 -> +1
        cnt += 1

print(cnt)
