# 18575 풍선팡 보너스 게임

import sys
sys.stdin = open('18575.txt', 'r')
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    row_sum = [sum(row) for row in grid]
    col_sum = [sum(grid[i][j] for i in range(N)) for j in range(N)]

    scores = []

    for i in range(N):
        for j in range(N):
            total = row_sum[i] + col_sum[j] - grid[i][j]
            scores.append(total)
    max_score_diff = 0
    for i in range(len(scores)):
        for j in range(i+1, len(scores)):
            max_score_diff = max(max_score_diff, abs(scores[i] - scores[j]))

    print(f'#{test_case} {max_score_diff}')
    
    
    
# 1시 17분 시작