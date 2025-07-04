import heapq

def solution(scoville, K):
    answer = 0
    # for i in scoville:
    #     heapq.heappush(heap,i) # 이 풀이는 nlogn
    heapq.heapify(scoville)
    
    while len(scoville) >= 2 and scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        c = a + (b * 2)
        heapq.heappush(scoville, c)
        answer += 1
    if scoville[0] < K:
        return -1
    return answer