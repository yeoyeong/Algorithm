def max_rhyme_pairs(n, L, F, words):
    # 접미사가 F 이상 맞는 쌍 찾기
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if words[i][-F:] == words[j][-F:]:
                pairs.append((i, j))

    # 유사 라임 쌍을 최대한 많이 만들기
    used = [False] * n
    max_pairs = 0
    
    for i, j in pairs:
        if not used[i] and not used[j]:
            used[i] = True
            used[j] = True
            max_pairs += 1
    
    return max_pairs


T = int(input())
for _ in range(T):
    n, L, F = map(int, input().split())
    words = input().split()
    result = max_rhyme_pairs(n, L, F, words)
    print(result)
