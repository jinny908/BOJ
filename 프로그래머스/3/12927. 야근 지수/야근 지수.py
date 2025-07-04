import heapq
def solution(n, works):
    works = [-w for w in works]
    heapq.heapify(works)
    
    for _ in range(n):
        if works[0] == 0:
            break
            
        max_work = heapq.heappop(works)
        heapq.heappush(works, max_work + 1)
        
    return sum(w**2 for w in works)
        