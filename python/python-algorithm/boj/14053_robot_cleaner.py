
def q1(arr, i, j):
    if arr[i][j] == 0:
        arr[i][j] = 2
    return arr

def q2(arr, i, j):
    dir = [0, 1, 2, 3]
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    stack = []
    for k in range(4):
        nr = r + di[i]
        nc = c + dj[i]
        stack.append(arr[nr][nc])

    return

def q3(arr, i, j):
    return





N, M = list(map(int, input().split()))  # 방 N*M
r, c, d = list(map(int, input().split()))
# 로봇청소기가 처음 있는 좌표 (r,c) # 로봇청소기가 바라보는 방향 d0 북 1 동 2 남 3 서
arr = [list(map(int, input().split())) for _ in range(M)]
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
    # 일단 탐색할좌표 변수 만들어준다
    nr = r + di[i]
    nc = c + dj[i]
    stack.append(arr[nr][nc])
    # 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if 0 not in stack:
        # 바라보는 방향을 유지한 채로 한칸 후진할 수 있다면
        # 북 -> 남 / 동 -> 서 / 남 -> 북 / 서 -> 동
        # 후진했을때의 좌표 kr kc로 설정

        if i == 0:  # 북쪽을 바라보고 있었다면 ? 남쪽 좌표는 i = 2일때임.
            kr = nr + di[2]
            kc = nc + dj[2]
        elif i == 1:    # 동 -> 서
            kr = nr + di[3]
            kc = nc + dj[3]
        elif i == 2:    # 남 -> 북
            kr = nr + di[0]
            kc = nc + dj[0]
        elif i == 3:    # 서 -> 동
            kr = nr + di[1]
            kc = nc + dj[1]

            # kr kc가 2 또는 0 (후진가능) 이면 후진하고 반복, 후진불가 (1)이면 작동멈춤
            if arr[kr][kc] == 1:
                break
                # 아니면 무한반복하는데. 이때 while을 어디에 걸어줘야하는지?
    # 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    else:
        # 반시계 방향으로 90도 회전한다
        # 이때 지금 좌표는 nr nc임 ..
        for j in range(4):  # 그럼 4칸을 탐색할건데
            # 북-> 서 / 동 -> 북 / 남 -> 동 / 서 -> 남

            if i == 0:  # 북 -> 서
                lr = nr + di[3]
                lc = nc + dj[3]
            elif i == 1:    # 동 -> 북
                lr = nr + di[0]
                lc = nc + dj[0]
            elif i == 2:  # 남 -> 동
                lr = nr + di[1]
                lc = nc + dj[1]
            elif i == 3:  # 서 -> 남
                lr = nr + di[2]
                lc = nc + dj[2]
                # lr, lc가 0인 경우 한칸 전진
                if arr[lr][lc] == 0:
                    nr = lr
                    nc = lc







# 2의 개수를 센다 (청소한 칸)
count = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:   # list index out of range.. 왜?
            count += 1
print(count)