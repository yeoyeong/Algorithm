#그래프에서 특정 시간 후에 
# #각 노드(매장)에 도달할 확률을 계산하는 문제
import sys

def solve(T, edges):
    # 매장 초기 확률 설정 (A, B, C, D의 초기 확률은 동일)
    current_probs = {'A': 0.25, 'B': 0.25, 'C': 0.25, 'D': 0.25}
    
    # 간선 정보로 매장 간 확률 매트릭스 구축
    transitions = {key: {} for key in 'ABCD'}
    
    for start, end, prob in edges:
        prob = float(prob)
        transitions[start][end] = prob
    
    # T번 반복해서 확률을 업데이트
    for _ in range(T):
        next_probs = {key: 0.0 for key in 'ABCD'}
        
        for start in 'ABCD':
            for end in transitions[start]:
                next_probs[end] += current_probs[start] * transitions[start][end]
        
        current_probs = next_probs
    
    # 결과 출력 (각 매장의 확률을 퍼센트로 변환해서 출력)
    for store in 'ABCD':
        print(f"{current_probs[store] * 100:.2f}")

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    M = int(data[1])
    edges = [tuple(line.split()) for line in data[2:2+M]]
    
    solve(T, edges)
