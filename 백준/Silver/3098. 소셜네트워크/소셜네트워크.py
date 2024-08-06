import sys
from collections import defaultdict

def social_network(N, M, edges):
    # 초기 그래프 구성
    friends = defaultdict(set)
    for a, b in edges:
        friends[a].add(b)
        friends[b].add(a)
    
    days = 0
    new_friendships_per_day = []

    while True:
        new_friendships = set()
        # 매일 친구 관계 확장
        for person in range(1, N + 1):
            new_friends = set()
            for friend in friends[person]:
                # 친구의 친구를 모두 새로운 친구로 추가
                new_friends.update(friends[friend])
            # 자신을 제외한 새로운 친구 추가
            new_friends.discard(person)
            for new_friend in new_friends:
                if new_friend not in friends[person]:
                    new_friendships.add((min(person, new_friend), max(person, new_friend)))
        
        if not new_friendships:
            break
        
        # 새로운 친구 관계 추가
        for a, b in new_friendships:
            friends[a].add(b)
            friends[b].add(a)
        
        new_friendships_per_day.append(len(new_friendships))
        days += 1

    print(days)
    for count in new_friendships_per_day:
        print(count)

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()
    N, M = map(int, data[0].split())
    edges = [tuple(map(int, line.split())) for line in data[1:1+M]]
    social_network(N, M, edges)
