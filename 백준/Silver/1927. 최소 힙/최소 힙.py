# 힙(heapq)을 이용한 문제
# 0일땐 출력
# 나머지 자연수는 저장

import sys
import heapq

input = sys.stdin.readline

heap = []
n = int(input())



for _ in range(n):
    x = int(input())
    
    if x == 0:
        if heap:
            # 힙에서 가장 작은 수를 꺼내고 출력
            print(heapq.heappop(heap))
        else:
            # 힙이 비어 있으면 0을 출력
            print(0)
    else:
        # 자연수가 들어오면 힙에 추가
        heapq.heappush(heap, x)