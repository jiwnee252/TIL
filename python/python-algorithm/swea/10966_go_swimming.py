import sys
# sys.stdin = open("10966_input.txt", "r")
from collections import deque   # 덱쓰면 런타임 에러남..

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(arr, N, M):

    dist = [[-1] * M for _ in range(N)]             # 거리
    queue = deque()
    # queue = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':  # W기준으로
                queue.append([i, j])
                dist[i][j] = 0  # 물이면 거리 0으로 일단해줌

    while queue:
        x, y = queue.popleft()
        # x, y = queue.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1:   # 범위안에 잇고 아직 방문x
                dist[nx][ny] = dist[x][y] + 1   # 거리 +1해줌
                queue.append([nx, ny])

    return dist

T = int(input())  # 테스트 케이스 수
for test_case in range(1, T+1):
    N, M = map(int, input().split())  # N: 세로, M: 가로 크기
    arr = [list(input().strip()) for _ in range(N)]  # 격자 입력
    # arr = [input() for _ in range(N)]  # 격자 입력
    dist = bfs(arr, N, M)
    # print(dist)

    total_dist = 0
    for i in range(N):
        total_dist += sum(dist[i])

    print(f'#{test_case} {total_dist}')
