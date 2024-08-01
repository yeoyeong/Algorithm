import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline
n = int(input().strip())

data = [input().strip() for _ in range(n)]

#데이터를 좌표로 변환
matrix = [list(map(int, row.split())) for row in data]

WIN_MESSAGE = "HaruHaru"
LOSE_MESSAGE = "Hing"


# 이동 가능 방향 만큼 dfs를 실행 했을 때
# -1이면 성공
# 장외면 패배


#dfs
def dfs(x, y, grid, n, m):
    if grid[x][y] == -1:
            return True
    if grid[x][y] == 0:
            return False
    move = grid[x][y]
    directions = [(move, 0), (0, move)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m :
            if dfs(nx, ny, grid, n, m):
                return True

    return False


#중복 발생 가능성이 없기에 방문 체크는 제외했다
def count_grass_areas(grid):
    if dfs(0, 0, grid, n, n):
         return WIN_MESSAGE
    else:
         return LOSE_MESSAGE
         
    
result = count_grass_areas(matrix)

print(result)