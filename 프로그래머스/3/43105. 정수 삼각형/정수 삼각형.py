def solution(triangle):
    answer = 0
    l = len(triangle)
    dp = [[0]*(l+2) for _ in range(l+2)]
    for i in range(1,l+1):
        for j in range(1,i+1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i-1][j-1]
    answer = max(max(dp))
    return answer