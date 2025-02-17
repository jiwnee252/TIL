import sys
sys.stdin = open("12712.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # N = 가로세로 # M = 스프레이세기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    # 대각선 # 좌상 # 우상 # 좌하 # 우하
    ei = [-1, -1, 1, 1]
    ej = [-1, 1, -1, 1]

    max_kill1 = 0
    max_kill2 = 0

    #상하좌우
    for i in range(N):
        for j in range(N):
            kill1 = arr[i][j]
            for d in range(4):  # ni nj는 <= N
                for k in range(1, M):
                    ni = i + di[d]*k
                    nj = j + dj[d]*k
                    if 0 <= ni < N and 0 <= nj < N:
                        kill1 += arr[ni][nj]
            if max_kill1 < kill1:
                max_kill1 = kill1
    #대각선
    for i in range(N):
        for j in range(N):
            kill2 = arr[i][j]
            for e in range(4):
                for k in range(1, M):
                    ni = i + ei[e]*k
                    nj = j + ej[e]*k
                    if 0 <= ni < N and 0 <= nj < N:
                        kill2 += arr[ni][nj]
            if max_kill1 < kill2:
                max_kill1 = kill2

    # print(kill1, kill2)
    print(f'#{test_case} {max_kill1 + max_kill2}')