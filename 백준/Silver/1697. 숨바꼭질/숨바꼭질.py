# 최단거리

#Input
# N(0 ≤ N ≤ 100,000)
# K(0 ≤ K ≤ 100,000)

# 이동 수단 X + 1, X - 1, 2X 

# 가장 빨리 N에서 K 가는 경우의 수 구하기

from collections import deque
import sys
input = sys.stdin.readline


def hide_and_seek(N, K):
    max_pos = 100001
    visited = [False] * max_pos
    
    # 큐 초기화, (현재 위치, 시간)
    queue = deque([(N, 0)])
    visited[N] = True
    
    while queue:
        current_pos, cnt = queue.popleft() #ex deque([(N, 1)]) => deque([])
        
        # 동생의 위치에 도달한 경우
        if current_pos == K:
            return cnt
        
        # 이동 가능한 세 위치를 확인
        for next_pos in (current_pos - 1, current_pos + 1, current_pos * 2):
            if 0 <= next_pos < max_pos and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, cnt + 1))




N, K = map(int, input().strip().split(" "))

result = hide_and_seek(N, K)
print(result)
