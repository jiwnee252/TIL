import sys
sys.stdin = open("9490_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    max_sum = 0

    for i in range(N):
        for j in range(M):
            f_sum = arr[i][j]   # 기준칸의값
            for d in range(4):   # 4방향.. 1칸
                for h in range(1, arr[i][j]+1):   # 상하좌우 arr[i][j]칸씩 추가로 터질때
                    bi = i + di[d] * h
                    bj = j + dj[d] * h
                    if 0 <= bi < N and 0 <= bj < M:
                        f_sum += arr[bi][bj]
            if max_sum < f_sum:
                max_sum = f_sum

    print(f'#{test_case} {max_sum}')
