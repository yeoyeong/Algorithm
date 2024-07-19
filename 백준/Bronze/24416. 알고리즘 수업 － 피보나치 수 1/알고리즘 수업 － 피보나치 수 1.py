number = int(input())
def fib(n) :
    if n == 1 or n == 2:
        return 1;  # 코드1
    return (fib(n - 1) + fib(n - 2))

# 메모이제이션을 이용한 재귀 호출 방식
def fib_memo(n, memo):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    memo[n] = result
    return result

def fibonacci(n):
    # 초기 예외 처리
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # 배열 f 초기화 및 초기값 설정
    f = [0] * (n + 1)
    f[1] = f[2] = 1

    # 피보나치 수열 계산
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    # n번째 피보나치 수 반환
    return f[n]

# result_1 = fib(number)
# result_2 = fibonacci(number)

# 실행 횟수 출력 함수
def count_executions(n):
    # 피보나치 수 계산 (재귀 호출)
    memo = {}
    # fib_result = fib(n)
    fib_result = fib_memo(n, memo)
    # 피보나치 수 계산 (동적 프로그래밍)
    fibonacci_result = fibonacci(n)
    
    # 재귀 호출의 실행 횟수는 피보나치 수와 동일
    count1 = fib_result
    
    # 동적 프로그래밍의 실행 횟수는 (n-2)
    count2 = n - 2
    
    return count1, count2

result = count_executions(number)
print(result[0], result[1])