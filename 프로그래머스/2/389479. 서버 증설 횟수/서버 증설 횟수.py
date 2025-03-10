def solution(players, m, k):
    server = [1] * 24 # 기본 1개 가동
    answer = 0
    for i in range(24):
        if players[i] >= server[i] * m:
            add = (players[i] // m) - server[i] + 1 
            answer += add
            for j in range(i,min(24,i+k)): # min 으로 초과 방지
                server[j] += add
    return answer 
    
