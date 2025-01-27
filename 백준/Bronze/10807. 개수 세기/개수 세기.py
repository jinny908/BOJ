import sys

n = int(input())
lst = list(map(int, input().split()))
v = int(input())

cnt = 0
for i in range(n):
    if lst[i] == v:
       cnt += 1

print(cnt)