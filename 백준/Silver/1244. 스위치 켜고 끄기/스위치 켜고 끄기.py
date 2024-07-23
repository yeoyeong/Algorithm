# 1 = on  0 = off

# 남학생
# 받은 수의 배수의 스위치 변경
# 여학생
# 받은 수 중심으로 대칭이 같은 스위치만 변경


# Input
# 1. 스위치 개수 
# 2. 스위치 스테이트
# 3. 학생수 < 100
# 4 ~ 받은 수 + 성별 
    # 남학생 1 여학생 2

# 예시 
# 0 1 0 1 0 0 0 1

# 남학생 실행
# 0 1 1 1 0 1 0 1

# 여학생 실행
# 1 0 0 0 1 1 0 1

import sys;

switch_cnt = int(sys.stdin.readline())
switch_state = list(map(int, sys.stdin.readline().split()))
student_cnt = int(sys.stdin.readline())

#학생수 
students=[]

#스위치 결과값
result=switch_state

#학생 별 작업 인풋
for cnt in range(student_cnt):
    students.append(list(map(int, sys.stdin.readline().split())))

#스위치 변경 함수
def useChange(number):
    if number == 0:
        return 1
    else:
        return 0

# 남학생 작업
def useSwitchChangeMan(number):
    # print(number, switch_cnt)
    for i in range(number, switch_cnt+1, number):
        change_num = useChange(result[i-1])
        result[i-1] = change_num


# 여학생 작업
def useSwitchChangeWoman(number):
    left = number - 1
    right = number - 1
    
    result[number-1] = useChange(result[number-1])

    while left >= 0 and right < switch_cnt and result[left] == result[right]:
        result[left] = useChange(result[left])
        result[right] = useChange(result[right])
        left -= 1
        right += 1


    

#학생 별 작업
for student in students:
    if student[0] == 1:
        useSwitchChangeMan(student[1])
        # result.append(2)
    elif student[0] == 2:
        useSwitchChangeWoman(student[1])


# 결과 출력
for i in range(switch_cnt):
    if i > 0 and i % 20 == 0:
        print()  # 20개마다 줄바꿈
    print(switch_state[i], end=' ')
print()  # 마지막 줄바꿈 추가