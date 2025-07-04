import heapq

def solution(jobs):
    time = 0
    i = 0
    answer = 0
    cnt = len(jobs)
    jobs.sort(key=lambda x:x[0])
    heap = []
    
    while i < cnt or heap:
        while i < cnt and jobs[i][0] <= time:
            request_time, duration = jobs[i]
            heapq.heappush(heap,(duration,request_time))
            i += 1
            
        if heap:
            duration, request_time = heapq.heappop(heap)
            time += duration
            answer += time - request_time 
        else:
            time = jobs[i][0]
        
    return answer//cnt