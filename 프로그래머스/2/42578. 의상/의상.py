def solution(clothes):
    dictionary = {}
    
    for name, kind in clothes:
        if kind in dictionary:
            dictionary[kind] += 1
        else:
            dictionary[kind] = 1
    answer = 1
    for v in dictionary.values():
        answer *= (v+1)
        
    return answer - 1
        