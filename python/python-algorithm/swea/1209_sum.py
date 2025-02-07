import sys
sys.stdin = open("1209_sum.txt", "r")

T = 10
for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    row_sum = 0  # 각 행의 합
    max_row = 0  # 각 행의 합 중 최댓값
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
        if max_row < row_sum:
            max_row = row_sum

    max_col = 0      # 각 열의 합
    col_sum = 0      # 각 열의 합 중 최댓값
    for j in range(100):
        col_sum = 0
        for i in range(100):
            col_sum += arr[i][j]
        if max_col < col_sum:
            max_col = col_sum

    d_lr_sum = 0    # 좌 -> 우 대각선의 합
    d_rl_sum = 0    # 우 -> 좌 대각선의 합

    for i in range(100):  # j는 필요ㄴㄴ인듯..
        d_lr_sum += arr[i][i]

    for i in range(100):
        for j in range(100):  # 하나씩돌면서..대각선이니깐 100-i + j가 100이될때
            if i + j == 100:
                d_rl_sum += arr[100-i][j]

    result = max(max_row, max_col, d_lr_sum, d_rl_sum)
    print(f'#{test_case} {result}')