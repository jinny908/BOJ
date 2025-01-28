n = input()
ans = [0] * 10
for i in range(len(n)):
    num = int(n[i])
    if num == 6 or num == 9:
        if ans[6] <= ans[9]:
            ans[6] += 1
        else:
            ans[9] += 1
    else:
        ans[num] += 1
print(max(ans))