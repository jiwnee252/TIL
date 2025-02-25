N, M = list(map(int, input().split()))  # 방 N*M
r, c, d = list(map(int, input().split()))
# print(r, c, d) # 로봇청소기가 처음 있는 좌표 (r,c)
# 로봇청소기가 바라보는 방향 d0 북 1 동 2 남 3 서
arr = [list(map(int, input().split())) for _ in range(M)]
# print(arr)
# (i,j) == 0 일경우 청소안됨 / 1 일경우 벽
# 로봇청소기 있는칸 항상0
# 동서남북 중 1줄이상은 모두1임

# 로봇청소기가 청소하는 칸의개수


# 북 동 남 서 0 1 2 3
dir = [0, 1, 2, 3]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


# 청소된칸을 2라고하고
# 현재칸이 0인경우 2를센다
# 현재칸 동서남북 중 0이 없는경우,
# 현재칸 동서남북 중 0이 있는경우,

# 북쪽을 바라보고 있으면 -> 남쪽으로 후진
# 동쪽을 바라보고 있으면 -> 서쪽으로 후진
# 남쪽을 바라보고 있으면 -> 북쪽으로 후진
# 서쪽을 바라보고 있으면 -> 동쪽으로 후진

for i in range(len(dir)):
    if arr[r][c] == dir[i]:
        nr = r + di[i]
        nc = c + dj[i]

        if arr[nr][nc] == 0:    # 현재 칸이 아직 청소되지 않은 경우
            arr[nr][nc] = 2     # 청소한 것으로 표시해줌
            # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
            if dir[i] == 0:     # 후진한다
                mr = nr + di[2]
                mc = mr + dj[2]
            elif dir[i] == 1:
                mr = nr + di[3]
                mc = mr + dj[3]
            elif dir[i] == 2:
                mr = nr + di[0]
                mc = mr + dj[0]
            elif dir[i] == 3:
                mr = nr + di[1]
                mc = mr + dj[1]

                if arr[mr][mc] == 1:
                    break               # 후진할 수 없다면 작동을 멈춘다.