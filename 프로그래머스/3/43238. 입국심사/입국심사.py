def solution(n, times):
    # n 값은 기다리는 사람 수
    # times 배열에 담겨있는 시간 = 심사관 마다 심사에 걸리는 시간
    # 즉 len(times) 가 심사관 수
    # n 값이 최대 10억이기에 log n 의 풀이로 접근해야한다.
    # 가능한 풀이, heapq, 이진 트리 등등 (다시 공부하기 이건)
    # left, right 는 총 심사에 걸리는 시간 기준
    left = 1
    right = max(times) * n
    answer = right # 최대치로 초기화 
    
    while left <= right:
        mid = (left + right) // 2
        total = sum(mid // time for time in times)
        
        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer