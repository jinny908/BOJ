n = int(input())

for _ in range(n):
    a, b = map(str, input().split())
    if len(sorted(a)) != len(sorted(b)):
        print("Impossible")
    elif sorted(a) == sorted(b):
        print("Possible")
    else:
        print("Impossible")


