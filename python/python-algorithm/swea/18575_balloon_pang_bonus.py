import sys
sys.stdin = open("18575.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    balloon = [list(map(int, input().split())) for _ in range(N)]

    # di = [-1, 1, 0, 0]
    # dj = [0, 0, -1, 1]  # 상하좌우


    score_list = []
    # 2번해야함
    for i in range(N):
        for j in range(N):
            score = 0     # 점수
            for d in range(N):
                score += balloon[d][j]
                score += balloon[i][d]
            score = score - balloon[i][j]
            score_list.append(score)
    result = max(score_list) - min(score_list)
    print(f'#{test_case} {result}')