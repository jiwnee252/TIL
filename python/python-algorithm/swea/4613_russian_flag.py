import sys
sys.stdin = open("4613_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # 국기 가로 M 세로 N.
    flag = [list(map(str, input())) for _ in range(N)]
    print(N)
    print(M)
    print(flag)

    count_w = 0
    count_b = 0
    count_r = 0

    for i in range(N):
        for j in range(M):

            if i == 0 and flag[i][j] != 'W':
                flag[i][j] = 'W'
            if i == N-1 and flag[i][j] != 'R':
                flag[i][j] = 'R'
    # wbr 줄마다 카운트


    # print(f'#{test_case} {result}')
    )