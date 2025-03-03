import sys
sys.stdin = open("1226_maze1.txt", "r")

def search_update(now_pos, pos, maze):  # 현재위치 now_pos 갈수있는좌표 pos 미로 maze

    # 상하좌우
    # di = [-1, 1, 0, 0]
    # dj = [0, 0, -1, 1]

    if maze[][] == 0:  # 만약 좌표이동했는데 0이면
        pos.append()


    return maze


def can_go(start, end, maze):   # 갈수있는지 없는지를 판단하는 함수
    pos = [start]  # pos: 갈수있는 좌표리스트. 일단 start좌표를 pos에넣는다
    while len(pos) != 0:   # 갈수있는 좌표가 남아 있으면
        now_pos = pos.pop(0)  # 현재좌표를 pos의 첫번째좌표로 갱신하고
        maze[now_pos[0]][now_pos[1]] = -1   # 방금지난좌표 탐색했다고 -1표시한다

        pos = search_update(now_pos, maze, pos)   # 갈수있는좌표리스트 = 4방향탐색후 남은 좌표리스트
        # 갈수있는 좌표중 도착점이 있는지
        if end in pos:
            return 1    # 도달가능
        else:
            return 0   # 도달불가














T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 1 벽 0 길 2 출발점 3 도착점
    maze = [list(map(int, input())) for _ in range(16)]

    # 일단 출발점 도착점을 찾는다
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = [i, j]   # 출발점을 찾는다
            if maze[i][j] == 3:
                end = [i, j]   # 도착점을 찾는다

