import sys
input = sys.stdin.readline 

n = int(input())


words = [input().strip() for _ in range(n)] 


#중복 제거
new_words = list(set(words))

# new_words.sort()
# new_words.sort(key=len)

# 길이 우선, 길이가 같다면 알파벳 순서로 정렬
new_words.sort(key=lambda x: (len(x), x))

print("\n".join(new_words))