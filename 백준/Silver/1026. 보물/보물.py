



# 문제 해석
# 입력값 - 길이가 N인 정수 배열 A와 B
# S = A[0] × B[0] + ... + A[N-1] × B[N-1]

# S의 최솟값을 출력을 위해
# A의 수를 재배열

import sys
input = sys.stdin.readline 

# def solve_treasure_problem(n, A, B):
#     # 배열 A를 오름차순 정렬
#     A.sort()
#     # 배열 B를 내림차순 정렬
#     B.sort(reverse=True)
    
#     # 최소 합 계산
#     minimum_sum = sum(a * b for a, b in zip(A, B))
#     return minimum_sum


# 최소값 출력
def solve_treasure_problem(n, A, B):
    A.sort()
    
    # 최소 합 계산
    minimum_sum = sum(a * b for a, b in zip(A, sorted(B, reverse=True)))
    return minimum_sum

    
n = input()


A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

# 결과 출력
result = solve_treasure_problem(n, A, B)
print(result)
