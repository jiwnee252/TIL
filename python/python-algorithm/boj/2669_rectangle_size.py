# r1 = list(map(int, input().split()))
# r2 = list(map(int, input().split()))
# r3 = list(map(int, input().split()))
# r4 = list(map(int, input().split()))

# rec = [list(map(int, input().split())) for _ in range(4)]

# 1이상 100이하이므로 100*100 배열 만들어준다
arr = [[0] * 100 for _ in range(100)]

for _ in range(4):
    rectangle = list(map(int, input().split()))  # 직사각형 4개 인풋 받음
    # print(rectangle)
    for i in range(rectangle[0], rectangle[2]) :
        for j in range(rectangle[1],rectangle[3]):
            arr[i][j] = 1

# print(arr)

# 1의 개수를 세준다
count = 0
for k in range(100):
    for m in range(100):
        if arr[k][m] == 1:
            count += 1

print(count)