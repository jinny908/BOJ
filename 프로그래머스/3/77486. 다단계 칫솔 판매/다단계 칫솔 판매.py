import math

def solution(enroll, referral, seller, amount):
    n = len(enroll)
    parentTree = dict(zip(enroll, referral))
    answer = dict(zip(enroll, (0 for _ in range(n))))
    
    for i in range(len(seller)):
        income = amount[i] * 100
        whosell = seller[i]
        
        while True:
            if income < 10:
                answer[whosell] += income
                break
            else:
                answer[whosell] += math.ceil(income * 0.9)
                if parentTree[whosell] == '-':
                    break
                income = math.floor(income * 0.1)
                whosell = parentTree[whosell]
                 
    return list(answer.values())