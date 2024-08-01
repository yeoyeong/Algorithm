#n개만큼 들어온 문자열을 뒤집는 문제

import sys
input = sys.stdin.readline


n, m = map(int, input().split())

numbers = [input().strip() for _ in range(n)]


for number in numbers:
    number
    reversed_number = number[::-1]
    print(reversed_number)
