import sys
input = sys.stdin.readline 
import heapq

def minimum_votes_to_win(n, votes):
    if n == 1:
        return 0
    dasom = votes[0]
    other_votes = [-vote for vote in votes[1:]]  # 최대 힙을 사용하기 위해 음수로 변환
    heapq.heapify(other_votes) #other_votes를 힙으로 변환

    additional_votes = 0
    
    while other_votes and -other_votes[0] >= dasom:
        max_other_votes = -heapq.heappop(other_votes)  
        max_other_votes -= 1  
        dasom += 1  
        additional_votes += 1
        heapq.heappush(other_votes, -max_other_votes) 
    
    return additional_votes

n = int(input())
numbers = list(int(input()) for _ in range(n))

result = minimum_votes_to_win(n, numbers)
print(result)