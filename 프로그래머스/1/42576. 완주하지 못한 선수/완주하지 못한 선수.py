from collections import Counter
def solution(participant, completion):
    result = Counter(participant) - Counter(completion)
    return list(result.keys())[0]
    
    # hashDict = {}
    # sumHash = 0
    # # 1. Hash : Make the dictionary of participant
    # # 2. Participant 의 sum(hash) 구하기
    # for i in participant:
    #     hashDict[hash(i)] = i
    #     sumHash += hash(i)
    # # 3. completion의 sum(hash) 빼기
    # for j in completion:
    #     hashDict[hash(j)] = j
    #     sumHash -= hash(j)
    # return hashDict[sumHash]
    