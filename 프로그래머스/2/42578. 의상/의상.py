def solution(clothes):
    dic = {}
    
    for i, j in clothes:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1
    # return dic
    answer = 1
    for i in dic.values():
        answer *= (i + 1)
    
    return answer - 1