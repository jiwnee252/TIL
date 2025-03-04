def can_go(start, end, maze):  # jump도 받아와야..
    count = 0   # 경로의 길이
    queue = [start]   # 갈수있는좌표. 일단 출발점을 넣는다

    di = [-1, 1, 0, 0]  # 상하좌우
    dj = [0, 0, -1, 1]

    while True:   # 계속 탐색
        # 큐의 첫번째 좌표를 꺼내서 해당 좌표의 상하좌우를 탐색한다
        now_pos = queue.pop(0)   # 현재 좌표
        now_x, now_y = now_pos   # 현재 x좌표 y좌표
        for d in range(4):  # 상하좌우 탐색
            if 0 <= now_x + di[d] < N and 0 <= now_y + dj[d] < N:   # 미로의 범위를 벗어나지 않는지 확인
                if maze[now_x + di[d]][now_y + dj[d]] == 0:  # 만약 0이면 통로이므로
                    new_x = now_x + di[d]   # 탐색한 x좌표 y좌표
                    new_y = now_y + dj[d]
                    queue.append([new_x, new_y])  # 큐에 저장한다.
                    count += 1

        if end in queue:
            return count
        else:
            return -1


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 출발점 도착점 점프대의 좌표를 구한다
            if maze[i][j] == 2:
                start = [i, j]
            if maze[i][j] == 3:
                end = [i, j]
            if maze[i][j] == 4:
                jump = [i, j]

    print(f'#{test_case} {can_go(start, end, maze)}')
