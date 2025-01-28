import sys
input = sys.stdin.readline

n, k = map(int, input().split())
students = [[0,0] for _ in range(6)] # [여, 남] * 6
cnt = 0

for i in range(n):
    s, y = map(int, input().split())
    # girls = 0, boys = 1
    students[y-1][s] += 1

for grade in students:
    for num in grade:
        cnt += num//k
        if num%k != 0:
            cnt += 1

print(cnt)

