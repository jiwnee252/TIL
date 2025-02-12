import sys
sys.stdin = open("1954.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    # N * N 의 달팽이를 출력하여라
    snail = list([0] * N for _ in range(N))
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    i = 0
    j = 0

    for a in range(1, N*N+1):
        snail[i][j] = a

    print(snail)


    # print(f'')