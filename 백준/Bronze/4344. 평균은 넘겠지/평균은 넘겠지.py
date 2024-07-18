# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다. 정답과 출력값의 절대/상대 오차는 10-3이하이면 정답이다.


# 풀의
# 점수를 모두 더 한다
# 학생 수로 나눈다
# 나온 평균점수와 학생의 점수를 비교한다

line = int(input())
students_score = []
avgs = []

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


for i in range(line):
    score = list(map(int, (input()).split()))
    students_score.append(score)

for line_students_score in students_score:
    student_count = line_students_score[0]
    scores = line_students_score[1:]
    print(calculate_percentage(student_count, scores))    
