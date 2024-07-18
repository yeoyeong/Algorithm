n = int(input())
star = "*"
blank_ = " "


for index in range(1, n + 1):
    print(f"{star * index}{blank_ * (n - index) * 2}{star * index}")
for index in range(n - 1, 0, -1):
    print(f"{star * index}{blank_ * (n - index) * 2}{star * index}")