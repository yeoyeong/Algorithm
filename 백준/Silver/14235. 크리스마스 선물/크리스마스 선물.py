#힙 문제
#최대힙은 음수를 사용해서 구함
import heapq
import sys

input = sys.stdin.read
data = input().splitlines()

heap = []

for line in data:
    # 선물 정보를 받음
    if line == "0":
        # 힙에서 가장 큰 선물을 꺼냄
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(-1)
    else:
        # 선물을 힙에 넣음
        presents = list(map(int, line.split()))
        for present in presents[1:]:
            heapq.heappush(heap, -present)
