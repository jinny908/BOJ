def gcd(a,b): # 유클리드 호제법을 이용한 최대공약수 구하기
    while b != 0:
        a, b = b, a % b
    return a

def check(gcd, array):
    for num in array:
        if num % gcd == 0:
            return False
    return True

def solution(arrayA, arrayB):
    result_a = arrayA[0]
    for num in arrayA[1:]:
        result_a = gcd(result_a,num)
    
    result_b = arrayB[0]
    for num in arrayB[1:]:
        result_b = gcd(result_b,num)
        
    # result_a 가 b 나눌 수 있는지 체크
    check_a = result_a if check(result_a, arrayB) else 0
    check_b = result_b if check(result_b, arrayA) else 0
            
    answer = max(check_a, check_b)
    return answer if answer != 0 else 0
    
    
    
    
            
        