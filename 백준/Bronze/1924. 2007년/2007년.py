# 1월1일 시작은 월요일
# 총 일수를 계산해서 요일로 변환 
# 총 일수를 7로 나눈 나머지

month, day = map(int, input().split())

month_2007 = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT", ]
total_days = sum(month_2007[m] for m in range(1, month)) + day
result = week[total_days%7]

print(result)
