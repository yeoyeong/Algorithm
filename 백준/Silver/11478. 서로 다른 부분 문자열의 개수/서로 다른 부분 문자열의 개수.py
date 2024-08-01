s = input()

a = set()

# 모든 부분 문자열을 집합에 추가
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        a.add(s[i:j])

# 집합의 크기가 서로 다른 부분 문자열의 개수
print(len(a))
