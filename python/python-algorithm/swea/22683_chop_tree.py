from collections import deque

di = [-1, 0, 1, 0]  # 상 우 하 좌 (시계방향으로)
dj = [0, 1, 0, -1]
dir = 0  # 방향 # 처음엔 위를 바라보고 있다.

def bfs(field, N, K):

    tree_count = 0
    move_count = 0
    visited = [[False] * N for _ in range(N)]

    q = deque()

    x, y = start
    m, n = end

    q.append(x, y, 0, 0, 0)    # 시작x좌표 시작y좌표 방향 나무벤횟수 조작한횟수
    visited[x][y] = True   # 시작좌표 방문처리.

    while q:
        x, y, dir, tree_count, move_count = q.popleft()

        if x == m and y == n:       # 도착함
            return move_count

    for x in range(N):
        for y in range(N):
            now_x, now_y = q.popleft()[0], q.popleft()[1]
            now_dir = 0
            print(now_x)
            print(now_y)

            for d in range(4):
                nx, ny = now_x + di[d], now_y + dj[d]   #  새로운 좌표.
                if 0 <= nx < N and 0 <= ny < N and field[nx][ny] != 'T': # 범위 내에 있고, 이동이 가능하면
                    now_x, now_y = nx, ny        # 위치를 업데이트 해준다.
                elif 0 <= nx < N and 0 <= ny < N and field[nx][ny] == 'T': # 범위 내에 있는데 나무이면
                    tree_count += 1    # 나무를 베어준다
                    if tree_count == K:    # 나무를 최대로 베었으면 멈춤.
                        break
    return -1   # 목적지 도달불가

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    field = [list(map(str, input().strip())) for _ in range(N)]

    # 최단거리가 아니라. 최소 리모컨 조작 횟수임에 유의한다
    # G 이동가능 T 이동불가 나무 X 현재위치 Y 도착점


    # 일단 첫좌표부터. 이동할 좌표를 큐에 넣어준다.
    # 좌표를 꺼내서. 상하좌우 좌표 적어주고
    # 현재 방향에 따라 조작횟수 올려주고
    # 이동하면 조작횟수 올려주고 좌표 갱신해준다
    # 나무이면 일단 베고 좌표갱신, 나무 카운트
    # 나무 카운트했는데 k랑 같아지면 버린다.

    start = None
    end = None

    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                start = [i, j]
            if field[i][j] == 'Y':
                end = [i, j]

    print(f'#{test_case} {bfs(field, N, K)}')

    # 우회전: now_dir = (now_dir + 1) % 4
    # 좌회전: now_dir = (now_dir - 1) % 4

'''

def bfs(field, N, K, start, target):
    visited = set()
    
    x, y = start
    tx, ty = target
    
        
        # 좌회전 & 우회전
        for turn in [-1, 1]:
            new_dir = (dir + turn) % 4
            if (x, y, new_dir, cuts) not in visited:
                visited.add((x, y, new_dir, cuts))
                queue.append((x, y, new_dir, cuts, moves + 1))
        
        # 전진
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < N and 0 <= ny < N:
            if field[nx][ny] == 'G' or field[nx][ny] == 'Y':  # 이동 가능
                if (nx, ny, dir, cuts) not in visited:
                    visited.add((nx, ny, dir, cuts))
                    queue.append((nx, ny, dir, cuts, moves + 1))
            elif field[nx][ny] == 'T' and cuts > 0:  # 나무 베기 가능
                if (nx, ny, dir, cuts - 1) not in visited:
                    visited.add((nx, ny, dir, cuts - 1))
                    queue.append((nx, ny, dir, cuts - 1, moves + 1))
    
'''