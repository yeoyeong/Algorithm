# 좌표 압축
# 0부터 작은 숫자를 저장

import sys

# 입력 받기
n = int(input())
coords = list(map(int, input().split()))


# 중복 제거 및 정렬
sorted_unique_coords = sorted(set(coords))

# 좌표값을 딕셔너리에 저장
coord_dict = {coord: idx for idx, coord in enumerate(sorted_unique_coords)}

# 압축된 좌표 출력
compressed_coords = [coord_dict[coord] for coord in coords]
print(' '.join(map(str, compressed_coords)))

# for coord in coords:
    # print(coord_dict[coord], end=" ")