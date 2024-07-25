import sys
input = sys.stdin.readline


n = int(input())
sentences = [input().strip() for _ in range(n)]
new_sentences = []

for sentence in sentences:
    new_sentence = []
    for word in reversed(sentence.split(" ")):
        new_sentence.append(word)
    new_sentences.append(new_sentence) 
    new_sentence = []

for index, new_sentence in enumerate(new_sentences, start=1):
    print(f"Case #{index}: {' '.join(new_sentence)}")