N, M = list(map(int, input().split()))  # 방 N*M
r, c, d = list(map(int, input().split()))
# print(r, c, d) # 로봇청소기가 처음 있는 좌표 (r,c)
# 로봇청소기가 바라보는 방향 d0 북 1 동 2 남 3 서
arr = [list(map(int, input().split())) for _ in range(M)]
# print(arr)
# (i,j) == 0 일경우 청소안됨 / 1 일경우 벽 / 로봇청소기 있는칸 항상0 /
# 동서남북 중 1줄이상은 모두1임 -> 이 조건 왜있는거지

# 로봇청소기가 청소하는 칸의개수
# 북 동 남 서 0 1 2 3
dir = [0, 1, 2, 3]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
# 청소된칸을 2라고하고 # 현재칸이 0인경우 2를센다
# 현재칸 동서남북 중 0이 없는경우,   # 현재칸 동서남북 중 0이 있는경우,


for i in range(4):
    stack = []   # 탐색한 칸을 저장해줄 스택
    # 일단 첫칸에 청소표시로 2해주고
    arr[r][c] = 2
    # 첫칸 4방향을 탐색할건데
    nr = r + di[i]
    nc = c + dj[i]
    stack.append(arr[nr][nc])
    # 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if 0 not in stack:
        # 바라보는 방향을 유지한 채로 한칸 후진할 수 있다면
        # 북 -> 남 / 동 -> 서 / 남 -> 북 / 서 -> 동
        kr = nr + di[i]
        kc = nc + dj[i]
        if i == 0:  # 북쪽을 바라보고 있었다면 ? 남쪽 좌표는 i = 2일때임.

            ########다시하기.. 남쪽의좌표를판단해야지
            if arr[kr][kc] == 1:    # 벽이라 후진할 수 없으면
                break       # 작동 멈춤
            else:       # 후진할 수 있다면
                nr = kr     # 후진한다
                nc = kc
        elif i == 1: # 동
            if arr[kr][kc] == 1:
                break
            else:
                nr = kr
                nc = kc
        elif i == 2: # 남
            if arr[kr][kc] == 1:
                break
            else:
                nr = kr
                nc = kc
        elif i == 3: # 서
            if arr[kr][kc] == 1:
                break
            else:
                nr = kr
                nc = kc
        ## 후진했음 ..1번으로 돌아가야되는데.. 여기서 for while 너무헷갈리는데??
        #
    else: # 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        # 일단 반시계 방향으로 90도 회전한다
        # 이때 지금 좌표는 nr nc임 ..
        # 90도 회전했는데 앞칸이 빈칸인경우 그칸으로감
        for j in range(4):  # 그럼 4칸을 탐색할건데
           # 북-> 서 / 동 -> 북 / 남 -> 동 / 서 -> 남
            # 예를들어 내가 북쪽을 바라보고 있었다면 서쪽을 탐색해서 서쪽이 0인경우 이동한다.
            lr = nr + di[i]
            lc = nc + dj[i]
           if i == 0:   # 북
               if arr[lr][lc] == 0:
                   nr = lr
                   nc = lc
               else: break
           elif i == 1: # 동
           elif i == 2: # 남
           elif i == 3: # 서
           
            if arr[lr][lc]



'''
# 북동남서 4방향 중에
for i in range(4):
    # 로봇청소기가 처음 위치한 (r,c)의 값과 dir(방향 리스트) 을 비교
    # 방향대로 한칸 이동 후 r, c 좌표를 nr, nc로 갱신
    if arr[r][c] == dir[i]:
        nr = r + di[i]
        nc = c + dj[i]
        # (nr, nc)가 만약 0이라면 청소되지 않은 것이므로
        if arr[nr][nc] == 0:
            arr[nr][nc] = 2     # 청소한 것으로 표시
            # (nr, nc)의 주변 4칸 탐색
            for k in range(4):
                # 주변 4칸의 좌표
                kr = nr + di[k]
                kc = nc + dj[k]
                # 만약 주변 4칸 중 0이 없는 경우


                if arr[kr][kc] != 0:
                    # 후진한다
                    # 이때 후진 방향은: (nr, nc)가 바라보고있던 방향 i
                    # 북 -> 남 / 동 -> 서 / 남 -> 북 / 서 -> 동   # 후진
                    if dir[i] == 0:
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
                else: # 후진 가능하다면
                    # 반시계방향 90도회전해서 1칸전진
                    # 북-> 서 / 동 -> 북 / 남 -> 동 / 서 -> 남
                    if dir[i] == 0:
                        lr = mr + di[3]
                        lc = mc + dj[3]
                    elif dir[i] == 1:
                        lr = mr + di[0]
                        lc = mc + dj[0]
                    elif dir[i] == 2:
                        lr = mr + di[1]
                        lc = mc + dj[1]
                    elif dir[i] == 3:
                        lr = mr + di[2]
                        lc = mc + dj[2]     # 한칸 전진 했음.

                        if arr[lr][lc] == 1:
                            break


'''
# 2의 개수를 센다 (청소한 칸)
count = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:   # list index out of range.. 왜?
            count += 1
print(count)