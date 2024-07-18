line = int(input())
students_score = []

# 평균을 넘는 학생들의 비율을 계산하는 함수
def calculate_percentage(student_count, scores):
    total_score = int(sum(scores))
    avg_score = total_score/student_count
    above_students = 0
    for score in scores:
        if score > avg_score: # 평균을 넘는 학생 수 세기
            above_students += 1
    percentage_above_avg = (above_students / student_count) * 100
    return f"{percentage_above_avg:.3f}%"

# 각 테스트 케이스에 대해 입력을 받고, 학생 수와 점수를 리스트에 저장
for i in range(line):
    score = list(map(int, (input()).split()))
    students_score.append(score)

# 각 테스트 케이스에 대해 계산 및 결과 출력
for line_students_score in students_score:
    student_count = line_students_score[0]
    scores = line_students_score[1:]
    avg = calculate_percentage(student_count, scores)
    print(avg)


