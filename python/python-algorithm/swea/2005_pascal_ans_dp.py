import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')

    triangle = [[0] * N for _ in range(N)]

    for i in range(N):
        triangle[i][0] = 1
        triangle[i][i] = 1

    for i in range(N):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    for i in range(N):
        print(' '.join(map(str, triangle[i][:i + 1])))
