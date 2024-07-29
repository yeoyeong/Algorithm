import sys
input = sys.stdin.readline

# 테스트 케이스의 수를 입력받습니다.
n = int(input().strip())

ticket_numbers = list(map(int, input().strip().split()))

def find_smallest_missing_ticket(ticket_numbers):

    ticket_numbers.sort()

    smallest_missing = 1
    for ticket in ticket_numbers:
        if ticket == smallest_missing:
            smallest_missing += 1
        else:
            break
    
    return smallest_missing

result = find_smallest_missing_ticket(ticket_numbers)

print(result)
