import sys
input = sys.stdin.readline

n, k = map(int,input().split())

ans = []
idx = 0
lst = [i for i in range(1,n+1)]

for i in range(n):
    idx += k-1
    if idx >= len(lst):
        idx %= len(lst)
    ans.append(lst.pop(idx))

print('<',', '.join(map(str,ans)),'>',sep='')