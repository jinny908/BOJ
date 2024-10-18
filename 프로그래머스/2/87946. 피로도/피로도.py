import itertools

def solution(k, d):
    full_list = list(itertools.permutations(d))
    
    answer = []
    
    for p in full_list:
        total = 0
        new_k = k
        for i, j in p:
            if i > new_k:
                break
            else:
                new_k = new_k - j
                total += 1
        answer.append(total)
    return max(answer)
        