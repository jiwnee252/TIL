import sys
sys.stdin = open("1226_maze1.txt", "r")


def search_update(now_pos, pos, maze):  # 현재위치 now_pos, 갈 수 있는 좌표 pos, 미로 maze
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    now_i, now_j = now_pos  # 현재의 i좌표, j좌표

    for d in range(4):
        ni, nj = now_i + di[d], now_j + dj[d]
        # ni nj가 범위 안에 있고 / 0 길 또는 3 도착점 인 경우 이동함
        if 0 <= ni < 16 and 0 <= nj < 16:
            if maze[ni][nj] == 3:
                return 1
            if maze[ni][nj] == 0:
                pos.append([ni, nj])
            if maze[ni][nj] != 3:  # 도착점은 방문 표시하지 않음
                maze[ni][nj] = -1
    return pos


def can_go(start, end, maze):   # 갈수있는지 없는지를 판단하는 함수
    pos = [start]  # pos: 갈수있는 좌표리스트. 일단 start좌표를 pos에넣는다
    while pos:   # 갈수있는 좌표가 남아 있으면
        now_pos = pos.pop(0)  # 현재좌표를 pos의 첫번째좌표로 갱신하고
        if search_update(now_pos, pos, maze) == 1:
            return 1
    return 0

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(10):
    # 1 벽 0 길 2 출발점 3 도착점
    test_case = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    # 일단 출발점 도착점을 찾는다
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = [i, j]   # 출발점을 찾는다
            if maze[i][j] == 3:
                end = [i, j]   # 도착점을 찾는다


    print(f'#{test_case} {can_go(start, end, maze)}')