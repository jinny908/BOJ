import heapq

def solution(jobs):    
    answer, now, i = 0, 0, 0 # i: 처리 개수, now: 현재 시각
    start = -1 # 마지막 완료 시각
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]]) 
                # 소요시간, 요청시점 이렇게 heap 에 넣어야 우선순위가 적용된다
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0] # 현재 시각 + 소요 시간
            answer += (now - current[1]) # 답 = 현재 시각 - 들어온 시각
            i += 1
        else:
            now += 1
    
    return int(answer / len(jobs))