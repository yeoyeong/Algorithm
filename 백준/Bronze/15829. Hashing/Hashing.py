import sys
input = sys.stdin.readline 

n = int(input())
string = input().strip()

def char_to_number(char):
    return "abcdefghijklmnopqrstuvwxyz".index(char) + 1


def hash_function(string, base=31, mod=1234567891):
    hash_value = 0
    for i, char in enumerate(string):
        # hash_value += (ord(char) - ord('a') + 1) * (base ** i)
        hash_value += char_to_number(char) * (base ** i)
        hash_value %= mod
    return hash_value

print(hash_function(string))