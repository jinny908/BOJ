def solution(info, n, m):
    
    prev_dp = [[0] * m for _ in range(n)]
    prev_dp[0][0] = 1 # 초기 0번 물건 처리 전
    
    for a_cost, b_cost in info:
        curr_dp = [[0] * m for _ in range(n)]
        for a in range(n):
            for b in range(m):
                if prev_dp[a][b]:
                    # a 가 물건 훔칠 때
                    # _a_a = a 가 물건 훔칠 때 a
                    # _a_b = a 가 물건 훔칠 때 b
                    new_a_a = a + a_cost 
                    new_a_b = b
                    if new_a_a < n and new_a_b < m:
                        curr_dp[new_a_a][new_a_b] = 1
                    # b 가 물건 훔칠 때
                    new_b_a = a
                    new_b_b = b + b_cost
                    if new_b_a < n and new_b_b < m:
                        curr_dp[new_b_a][new_b_b] = 1
        prev_dp = curr_dp
            
    min_a = float('inf')
    for a in range(n):
        for b in range(m):
            if prev_dp[a][b]:
                if a < min_a:
                    min_a = a
    

    
    if min_a != float('inf'):
        return min_a
    else:
        return -1
                    