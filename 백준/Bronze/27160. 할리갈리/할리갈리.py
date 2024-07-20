import sys

def check_halligalli():
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    cards = {}


    #1부터 2*N까지 2씩 증가하는 포우문
    for i in range(1, 2*N, 2):
        card = data[i]
        count = int(data[i+1])  
        
        if card in cards:
            cards[card] += count
        else:
            cards[card] = count

    for count in cards.values():
        if count == 5:
            
            return "YES"
    
    return "NO"

result = check_halligalli()
print(result)