import sys
import heapq

input = sys.stdin.readline
n = int(input())
left = []
right = []

for _ in range(n):
    num = int(input())

    if not left or num <= - left[0]:
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))

    print(-left[0])




