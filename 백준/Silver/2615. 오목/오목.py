#오목
# 사이즈 19 x 19

# 승리 규칙
# 가로 / 세로 / 대각선 
# 5알 이면 승리
# 6할 이상은 X


# 입력된 바둑판의 상태를 보고 승리, 패배, 경기 중 판단
# 검은색, 흰색이 동시에 이기거나 두 군데 이상에서 동시에 이기는 경우는 없음

# 검은 바둑알 = 1
# 흰 바둑알 = 2


# 출력
# 검은색 승 1 
# 흰색 승 2
# 승부중 0
# 두번째 줄에 
# 승리한 바둑알 맨 왼쪽 좌표 출력


# 21 비교 대상
# 21 + 1
# 21 - 1 

# 21 - 19
# 21 - 19 -1
# 21 - 19 + 1

# 21 + 19
# 21 + 19 + 1
# 21 + 19 - 1

board = [list(map(int, input().split())) for _ in range(19)]
LINE = 19




def check_winner(board):
    # 방향 벡터 정의: 가로, 세로, 대각선 오른쪽 아래, 대각선 왼쪽 아래
    directions = [
        (0, 1),  # 가로
        (1, 0),  # 세로
        (1, 1),  # 대각선 오른쪽 아래
        (1, -1) # 대각선 왼쪽 아래
    ]

    # 주어진 좌표가 19x19 바둑판 내에 있는지 확인하는 함수
    def is_valid(x, y):
        return 0 <= x < 19 and 0 <= y < 19
    
    #6목인지 체크
    def check_six_stones(further_x, further_y, prev_x, prev_y, stone):
        if is_valid(further_x, further_y) and board[further_x][further_y] == stone:
            return False
        if is_valid(prev_x, prev_y) and board[prev_x][prev_y] == stone:
            return  False
        return True

    #모든 방향 탐색
    def check_directions(x, y, stone):
        for dx, dy in directions:
            cnt = 1
            stones = [[x,y]]
            #다음 위치
            nx, ny = x + dx, y + dy
            while is_valid(nx, ny) and board[nx][ny] == stone:
                cnt += 1
                stones.append([nx, ny])
                if cnt == 5:
                    further_x, further_y = nx + dx, ny + dy
                    prev_x, prev_y = x - dx, y - dy
                    if check_six_stones(further_x, further_y, prev_x, prev_y, stone):
                        leftmost_stone = min(stones, key=lambda stone: (stone[1], stone[0]))
                        return stone, leftmost_stone[0] + 1, leftmost_stone[1] + 1
                nx += dx
                ny += dy

        return None, None, None

    for x in range(LINE):
        for y in range(LINE):
            if board[x][y] != 0:
                stone = board[x][y]
                winner, win_x, win_y = check_directions(x, y, stone)
                if winner:
                    return winner, win_x, win_y
                
    return 0, 0, 0


#브루트포스 알고리즘가


# 승리 여부 확인
winner, win_x, win_y = check_winner(board)

# 결과 출력
print(winner)
if winner != 0:
    print(win_x, win_y, end='')