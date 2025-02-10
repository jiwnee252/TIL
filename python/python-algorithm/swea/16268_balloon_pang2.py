import sys
sys.stdin = open("16268.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # arr[i][j]의 상하좌우 칸이 arr[ni][nj] 라고할때
    # didj 방향별로더할값..

    # 구하는것 -> arr[i][j] 의 값 + 상하좌우칸 총 5개칸의값의합
    # arr[i][j]값을 기준으로
    # 상 하 좌 우 (4번) 반복해서 arr[ni][nj]의 값을 더해줌

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # f_sum = 기준칸의 값
    # max_sum = 최대합

    max_sum = 0

    for i in range(N):    # 0부터 N-1까지.
        for j in range(M):
            f_sum = arr[i][j]
            for d in range(4):  # 4방향탐색
                ni = i + di[d]   # i-1, i+1, i+0, i+0
                nj = j + dj[d]   # j+0, j+0, j-1, j+1
                if 0 <= ni < N and 0 <= nj < M:
                    f_sum += arr[ni][nj]
            if max_sum < f_sum:
                max_sum = f_sum

    print(f'#{test_case} {max_sum}')
