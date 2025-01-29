word1 = input()
word2 = input()

count1 = [0] * 26 # alphabet = 26
count2 = [0] * 26

for i in word1:
    count1[ord(i)-ord('a')]+=1 # ord('a') = 97
for i in word2:
    count2[ord(i)-ord('a')]+=1

ans = 0

for i in range(26):
    ans += abs(count1[i]-count2[i])
    # 갯수 차이가 음수가 될 수도 있기 때문에 abs 함수를 사용
    # ex) count2 에 'b' 가 더 많을 수도 있기 때문에 이 방식을 채용

print(ans)