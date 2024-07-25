import sys
input = sys.stdin.readline

number = input().strip()

#각 자리수 합
def sum_of_digits(num):
    return sum(int(add_num) for add_num in num)

#3의 배수 체크
def is_multiple_of_3(num):
    if num % 3 == 0:
        return "YES"
    else:
        return "NO"


def solve(num):
    """입력된 숫자를 3의 배수인지 확인하는 함수"""
    cnt = 0
    while len(num) > 1:
        num = str(sum_of_digits(num))
        cnt += 1
    result = is_multiple_of_3(int(num))
    return result, cnt

result, cnt = solve(number)

print(cnt)
print(result)
