import sys
input = sys.stdin.readline

# 테스트 케이스의 수를 입력받습니다.
n = int(input().strip())
result = []

def load_university_data(m):
    for _ in range(m):
        university, drinks = input().strip().split()
        test_case.append({
            'university': university,
            'drinks': int(drinks)
        })

for _ in range(n):
    m = int(input().strip())  # 각 테스트 케이스마다 대학의 수를 입력받습니다.
    test_case = []
    #대학 데이터 test_case에 불러오기
    load_university_data(m)
    #원하는 값 찾기
    result.append(max(test_case, key=lambda x: x['drinks'])['university'])
    #출력


print('\n'.join(result))