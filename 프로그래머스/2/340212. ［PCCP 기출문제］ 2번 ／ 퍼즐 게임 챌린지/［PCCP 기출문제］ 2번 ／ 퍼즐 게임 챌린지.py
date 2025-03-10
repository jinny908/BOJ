def solution(diffs, times, limit):
    def solve(lvl):
        total_time = times[0] # 첫 문제는 바로 풀 수 있
        for i in range(1,len(diffs)):
            if lvl >= diffs[i]:
                total_time += times[i]
            else:
                fail_cnt = diffs[i] - lvl
                total_time += fail_cnt * (times[i-1] + times[i]) + times[i]
                # total = 레벨 차이 * (curr_time + prev_time) + curr_time
            if total_time > limit:
                return False
        return True
    
    left, right = 1, max(diffs)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if solve(mid):
            answer = mid
            right = mid - 1 # 더 낮은 숙련도 가능한지 확인
        else:
            left = mid + 1
    
    return answer