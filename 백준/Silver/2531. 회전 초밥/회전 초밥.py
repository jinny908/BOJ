import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
belt = []
for _ in range(n):
    plate = input().strip()
    belt.append(int(plate))

belt.extend(belt[0:k-1])

max_plate = 0

for i in range(0,n):
    set_plate = belt[i:i+k]
    unique = set(set_plate)
    unique.add(c) # coupon 추가
    max_plate = max(max_plate, len(unique))

print(max_plate)