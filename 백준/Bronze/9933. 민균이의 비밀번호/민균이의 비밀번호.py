#문자를 뒤집었을 때 배열에 있는지 체크



import sys
input = sys.stdin.readline 


n = int(input())
words = list(str(input().strip()) for _ in range(n))

def find_password(words):
    for word in words:
        reversed_word = word[::-1]
        if reversed_word in words:
            length = len(reversed_word)
            middle_char = reversed_word[length // 2]
            return length, middle_char


len, middle_char = find_password(words)
print(len, middle_char)