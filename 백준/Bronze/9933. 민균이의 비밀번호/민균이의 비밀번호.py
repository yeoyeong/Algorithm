import sys
input = sys.stdin.readline 


n = int(input())
words = list(str(input().strip()) for _ in range(n))

def find_password(words):
    words_set = set(words)
    for word in words:
        reversed_word = word[::-1]
        if reversed_word in words_set:
            length = len(reversed_word)
            middle_char = reversed_word[length // 2]
            return length, middle_char


len, middle_char = find_password(words)
print(len, middle_char)
