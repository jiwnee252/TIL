import sys
sys.stdin = open("23894_5188_input.txt", "r")

# dfs_bfs
def dfs(N, arr):
    # 아래, 오른쪽
    di = [1, 0]
    dj = [0, 1]
    stack = [[0, 0, arr[0][0]]]
    min_sum = 9999
    while stack:   # 스택에 갈곳이 남아있으면
        si, sj, total_count = stack.pop()
        if si == N-1 and sj == N-1:
            min_sum = min(min_sum, total_count)
            continue
        for d in range(2):
            ni = si + di[d]
            nj = sj + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                stack.append([ni, nj, total_count + arr[ni][nj]])
    return min_sum

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{test_case} {dfs(N, arr)}')