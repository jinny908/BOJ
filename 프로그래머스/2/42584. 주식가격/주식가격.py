from collections import deque

def solution(prices):
    
    q = deque(prices)
    answer = []
    
    while q:
        time = 0
        stock = q.popleft()
        for i in q:
            time += 1
            if stock > i:
                break
        answer.append(time)
    return answer