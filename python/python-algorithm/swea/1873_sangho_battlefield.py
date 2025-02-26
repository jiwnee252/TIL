import sys
sys.stdin = open("1873_sangho.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    game = [list(map(str, input().split())) for _ in range(H)]
    N = int(input()) # len(command_list)
    command_list = list(input())
    change_dir = ['U', 'D', 'L', 'R']  # 이동 명령 리스트

    di = [-1, 1, 0, 0]  # 상 하 좌 우
    dj = [0 ,0, -1, 1]
    directions = ['^', 'v', '<', '>']
    tank_dir = 0
    # dr 0123


    for i in range(W):
        for j in range(H):
            if game[i][j] in directions:  # 탱크를 일단 찾는다
                if game[i][j] == '^':
                    # 해당 탱크의 방향을 저장한다
                    tank_dir = 0
                    tank_coor = [i, j]
                    break # 일단 초기탱크좌표,초기탱크방향 찾았으니까 탱크찾는건 브레이크함
    for command in command_list:
        # 이동일경우
        if command in change_dir:
            # 방향을 먼저 바꿔주고
            # 이동한다
            if command == 'U':
                tank_dir = 0
                ni = i + di[0]
                nj = j + dj[0]
            elif command == 'D':
                tank_dir = 1
                ni = i + di[1]
                nj = j + dj[1]
            elif command == 'L':
                tank_dir = 2
                ni = i + di[2]
                nj = j + dj[2]
            elif command == 'R':
                tank_dir = 3
                ni = i + di[3]
                nj = j + dj[3]
        # 발사일경우
        elif command == 'S':
            # 왼쪽을 바라보고 있으면 왼쪽으로 계속간다
            # 내 왼쪽에 *이나 # 가 있을때까지.
            # *면 .로 바꿔주고 #면 다음명령을 기다림.
            if tank_dir == 0:

            elif tank_dir == 1:

            elif tank_dir == 2:

            elif tank_dir == 3:

            

# 발사 -> 벽돌벽 : 평지로 변환
# 발사 -> 강철벽 : pass
# 발사 -> 맵 탈출 : pass
# 방향 먼저 바꾸고 -> 이동

    if wall == '*' :
        wall = '.'   # 평지로 바꿔준다.
    elif wall == '#':
        pass   # 아무 일도 일어나지 않고 다음 명령을 기다림.
