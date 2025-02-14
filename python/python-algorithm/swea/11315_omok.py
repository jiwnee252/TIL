import sys
sys.stdin = open("11315.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    # print(N)
    stone = [input().split() for _ in range(N)]
    # print(stone)
    row_count = 0
    col_count = 0
    # 가로
    for row in stone:
        if 'ooooo' in row:
            row_count += 1
        # print(row_count)



    print(stone)
# 세로

# 대각선

# print(f'#{test_case} {result}')