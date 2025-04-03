def cross(stones,k,mid):
    skip = 0
    for stone in stones:
        if stone - mid < 0:
            skip += 1
            if skip >= k:
                return False
        else:
            skip = 0
    return True

def solution(stones, k):
    left = 1
    right = max(stones)
    answer = 0
    
    
    
    while left <= right:
        mid = (left + right) // 2
        if cross(stones, k, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer