import sys
sys.stdin = open("1954.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # N * N 의 달팽이를 출력하여라
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    snail = [[0] * N for _ in range(N)]

    i = 0
    j = 0
    count = 1
    dr = 0   # [0,1,2,3]
    snail[i][j] = count
    count += 1

    while count <= N * N:
        ni = i + di[dr]
        nj = j + dj[dr]
        if 0 <= ni < N and 0 <= nj < N and snail[ni][nj]==0:
            i, j = ni, nj
            snail[i][j] = count
            count += 1
        else:
            dr = (dr+1) % 4

    print(f'#{test_case}')
    for lst in snail:
        print(*lst)

        # 런타임에러 ??