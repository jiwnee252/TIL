T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    field = [list(map(str, input())) for _ in range(N)]
    Q = int(input())
    commands = []

    for _ in range(Q):
        line = input().split()
        commands.append(line[1])
        # print(commands)

    di = [-1, 0, 1, 0]  # 북 동 남 서
    dj = [0, 1, 0, -1]

    start = []
    end = []

    for x in range(N):
        for y in range(N):
            if field[x][y] == 'X':
                start = [x, y]
            if field[x][y] == 'Y':
                end = [x, y]

    results = []

    for command in commands:
        now_x, now_y = start[0], start[1]
        now_dir = 0
        for cmd in command:
            if cmd == 'A':
                nx, ny = now_x + di[now_dir], now_y + dj[now_dir]   # 새로운좌표
                if 0 <= nx < N and 0 <= ny < N and field[nx][ny] != 'T':   # 범위내에있고 이동가능하다면
                    now_x, now_y = nx, ny   # 위치 업데이트
            elif cmd == 'R':
                now_dir = (now_dir + 1) % 4
            elif cmd == 'L':
                now_dir = (now_dir - 1) % 4


        if [now_x, now_y] == end:
            results.append(1)
        else:
            results.append(0)

        # print(results)

    print(f"#{test_case} {' '.join(map(str, results))}")