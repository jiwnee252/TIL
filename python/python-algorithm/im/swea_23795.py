# 23795  우주 괴물
import sys
sys.stdin = open('23795.txt', 'r')
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    map_data = [list(map(int, input().split())) for _ in range(N)]
    # print(map_data)
    visited = [[False]*N for _ in range(N)]
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # 상하좌우
    for i in range(N):
        for j in range(N):
            if map_data[i][j] == 2:
                monster_pos = (i, j)

    # print(monster_pos)

    x, y = monster_pos
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        while 0 <= nx < N and 0 <= ny < N:
            if map_data[nx][ny] == 1:
                break
            if map_data[nx][ny] == 0:
                visited[nx][ny] = True
            nx += dx
            ny += dy

    safe_zone = 0
    for i in range(N):
        for j in range(N):
            if map_data[i][j] == 0 and not visited[i][j]:
                safe_zone += 1

    print(f"#{test_case} {safe_zone}")
