import sys
input = sys.stdin.readline 
import heapq

dwarf = [int(input().strip()) for _ in range(9)]

# 난쟁이들의 키의 합을 구합니다.
total_sum = sum(dwarf)
result = []
found = False

# 브루트 포스 방법으로 2명을 제외하는 경우를 찾습니다.
for i in range(9):
    for j in range(i + 1, 9):
        if total_sum - dwarf[i] - dwarf[j] == 100:
            # i와 j를 제외한 나머지 난쟁이들을 출력합니다.
            for k in range(9):
                if k != i and k != j:
                    result.append(dwarf[k])
            result.sort()
            found = True
            break
    if found:
        break



for height in result:
    print(height)