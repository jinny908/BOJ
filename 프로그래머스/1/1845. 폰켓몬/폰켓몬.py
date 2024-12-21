def solution(nums):
    cnt = 1
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            cnt += 1
    max = len(nums) // 2
    return min(max,cnt)
        
        