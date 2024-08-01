#재귀함수문제
#별찍기

def shooting_stars(n):
    # 전체 크기 계산
    size = 4 * n - 3

    # 전체 크기의 정사각형 빈칸 배열 생성
    matrix = [[' ' for _ in range(size)] for _ in range(size)]


    # 한줄씩 채우기
    def fill_square(level, start, end):
        if level == 0:
            return
        for i in range(start, end + 1):
            matrix[start][i] = '*'
            matrix[end][i] = '*'
            matrix[i][start] = '*'
            matrix[i][end] = '*'
        fill_square(level - 1, start + 2, end - 2)
    
    # 재귀적으로 별을 채워 나감
    fill_square(n, 0, size - 1)
    
    # 결과 출력
    for row in matrix:
        print(''.join(row))

# N 입력 받기
n = int(input())

shooting_stars(n)

# 이해는 했는데 어려웠던 문제