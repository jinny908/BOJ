import heapq
def solution(operations):
    answer = []
    heap = []
    
    for o in operations:
        alphabet, number = o.split()
        number = int(number)
        
        if alphabet == 'I':
            heapq.heappush(heap, number)
        else:
            if heap:
                if number == -1:
                    heapq.heappop(heap)
                else:
                    heap.sort() # 오름차순 정렬
                    heap.pop() # 최댓값 삭제
    
    heap.sort()
    if heap:
        answer = [heap[-1],heap[0]]
    else:
        answer = [0,0]
    return answer