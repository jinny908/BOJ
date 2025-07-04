def solution(m, n, puddles):
    MOD = 1_000_000_007  # 문제에 따라 모듈러 필요할 수 있음 (없으면 제거 가능)
    
    # 물에 잠긴 위치들을 set으로 저장 (열, 행 순서로 변환)
    blocked = set((y, x) for x, y in puddles)

    # DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1  # 출발점은 항상 1

    for i in range(1, n + 1):     # 행 (y)
        for j in range(1, m + 1): # 열 (x)
            if (i, j) in blocked or (i == 1 and j == 1):
                continue
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

    return dp[n][m]