import sys
input = sys.stdin.readline

n, m = map(int, input().split())
value = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

dp[0][0] = value[0][0]

# 첫 줄은 dp 값 갱신
for j in range(1,m):
    dp[0][j] = dp[0][j-1] + value[0][j]

# 나머지 행 갱신
for i in range(1,n):
    to_right = [0] * m
    to_left = [0] * m

    # 오른쪽 방향으로 진행
    for j in range(m):
        if j == 0:
            to_right[j] = dp[i-1][j] + value[i][j]
        else:
            to_right[j] = max(dp[i-1][j], to_right[j-1]) + value[i][j]

    # 왼쪽 방향으로 진행
    for j in range(m-1,-1,-1):
        if j == m-1:
            to_left[j] = dp[i-1][j] + value[i][j]
        else:
            to_left[j] = max(dp[i-1][j], to_left[j+1]) + value[i][j]

    for j in range(m):
        dp[i][j] = max(to_left[j], to_right[j])


print(dp[n-1][m-1])