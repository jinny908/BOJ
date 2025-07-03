def solution(clothes):
    dict = {}
    
    for name, category in clothes:
        if category in dict:
            dict[category] += 1
        else:
            dict[category] = 1
    
    answer = 1
    for cnt in dict.values():
        answer *= (cnt + 1)
        
    return answer - 1