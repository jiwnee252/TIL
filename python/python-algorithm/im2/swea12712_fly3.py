import sys
sys.stdin = open("12712.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            di = [0, 1, 0, -1]
            dj = [1, 0, -1, 0]
            for k in range(4):
                for z in range(1, M):
                    ni, nj = i + di[k] * z, j + dj[k] * z
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
            if max_v < s:
                max_v = s
            di = [1, 1, -1, -1]
            dj = [1, -1, -1, 1]
            s = arr[i][j]
            for k in range(4):
                for z in range(1, M):
                    ni, nj = i + di[k] * z, j + dj[k] * z
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
            if max_v < s:
                max_v = s
    print(f'#{tc} {max_v}')
