# 각 의상은 특정 카테고리 존재
# 같은 카테고리에서 여러 개의 의상이 주어질 수 있음
# 의상을 조합하여 입을 수 있는 경우의 수를 계산

import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

t = int(data[0])  # 테스트 케이스 수
index = 1

for _ in range(t):
    n = int(data[index])  # 각 테스트 케이스의 의상 수
    index += 1
    
    clothes = defaultdict(int)
    
    for _ in range(n):
        name, category = data[index].split()
        clothes[category] += 1
        index += 1
    
    combinations = 1
    for count in clothes.values():
        combinations *= (count + 1)
    
    # 아무것도 입지 않은 경우는 제외
    print(combinations - 1)

# defaultdict 메서드
# 딕셔너리 형태
# 존재하지 않는 키에 접근하려고 할 때 자동으로 기본값을 생성해주는 특징이 있다.

# 기본값이 0인 defaultdict 생성
#counts = defaultdict(int)

# 존재하지 않는 키에 접근하려고 하면, 기본값 0이 자동으로 설정됨
# counts['apple'] += 1
# counts['banana'] += 1

# print(counts)  
# # 출력: {'apple': 1, 'banana': 1}

