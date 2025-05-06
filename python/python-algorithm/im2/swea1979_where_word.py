dr = [1, 0]   #  move = 0 이면 세로
dc = [0, 1]     # move = 1 이면 가로

def check(row, col, move):
    if move == 0:   # 세로 쓰기
        # 시작지점이 가장 윗 줄이고, 다음줄이 빈칸이면
        if row == 0 and puzzle[row+1][col] == 1:
            return True
        # 첫 줄이 아닐떄는, 위가 막혀있고, 아래가 뚫려있을 떄만
        if 1 <= row < N-1 and puzzle[row+1][col] == 1 and puzzle[row-1][col] == 0 :
            return True
    else:           # 가로 쓰기
        # 시작지점이 가장 왼쪽 줄이고, 다음 칸이 빈칸이면
        if col == 0 and puzzle[row][col+1] == 1:
            return True
        # 가장 왼쪽이 아닐때는, 왼쪽이 막혀있고, 오른쪽이 뚫려있을 때만
        if 1 <= col < N-1 and puzzle[row][col+1] == 1  and puzzle[row][col-1] == 0 :
            return True
    return False

def search(row, col):
    result = 0
    for i in range(2): # 가로랑 세로를 검사
        if check(row, col, i):  # 조사시작 가능한지 체크
            nr = row      # 한 위치에서 양 방향으로 조사 할 수 있으므로
            nc = col      # 원본을 그대로 둔 채 조사
            cnt = 1       # 첫 시작 글자 1개
            while True:
                nr = nr + dr[i] # 다음 위치 조사
                nc = nc + dc[i]
                # 다음 위치가 범위를 벗어나지 않고 빈칸이면
                if 0 <= nr < N and 0 <= nc < N and puzzle[nr][nc] == 1:
                    cnt += 1    # 한 칸 더 작성 가능
                else:
                    break       # 아니면 종료
            if cnt == K:        # 모든 조사를 완료했을때 K만큼만 입력가능하면
                result += 1     # 입력 가능 경우 1증가
    return result

'''
import sys
sys.stdin = open('1979.txt')  # 입력 파일 열기

T = int(input())  # 테스트 케이스 개수
for tc in range(1, T + 1):  # 각 테스트 케이스마다
    N, K = map(int, input().split())  # 퍼즐 크기 N, 단어 길이 K
    puzzle = [list(map(int, input().split())) for _ in range(N)]  # 퍼즐판

    result = 0  # 정답 개수

    dr = [1, 0]  # 세로 이동 (아래로 1칸), 가로 이동 (변화 없음)
    dc = [0, 1]  # 세로 이동 (변화 없음), 가로 이동 (오른쪽으로 1칸)

    for row in range(N):  # 모든 행을 하나씩
        for col in range(N):  # 모든 열도 하나씩
            if puzzle[row][col] != 1:  # 0이면 (막힌 칸이면) 그냥 넘어감
                continue

            for move in range(2):  # 두 방향 확인: 0 = 세로, 1 = 가로
                # 시작 가능한 자리인지 확인 (check 역할)

                if move == 0:  # 세로 방향
                    if row == 0:
                        # 맨 위줄이면 아래 칸만 1이면 시작 가능
                        if row + 1 < N and puzzle[row + 1][col] == 1:
                            pass
                        else:
                            continue
                    elif 1 <= row < N - 1:
                        # 위가 막혀있고, 아래가 뚫려있어야 시작점
                        if puzzle[row - 1][col] != 0 or puzzle[row + 1][col] != 1:
                            continue
                    else:
                        # 맨 아래줄이거나 조사 불가능한 위치
                        continue

                else:  # 가로 방향
                    if col == 0:
                        # 맨 왼쪽 칸이면 오른쪽만 뚫려있으면 시작 가능
                        if col + 1 < N and puzzle[row][col + 1] == 1:
                            pass
                        else:
                            continue
                    elif 1 <= col < N - 1:
                        # 왼쪽이 막혀있고, 오른쪽이 뚫려있어야 시작점
                        if puzzle[row][col - 1] != 0 or puzzle[row][col + 1] != 1:
                            continue
                    else:
                        # 맨 오른쪽 칸이거나 조사 불가능한 위치
                        continue

                # 시작점이 맞으면, 여기서부터 길이 세기 시작 (search 역할)
                cnt = 1  # 지금 이 칸부터 시작했으니까 길이 1
                nr = row
                nc = col

                while True:
                    nr += dr[move]  # 방향대로 다음 위치로 이동
                    nc += dc[move]

                    # 퍼즐 범위 안이고, 그 칸이 1이면 계속 진행
                    if 0 <= nr < N and 0 <= nc < N and puzzle[nr][nc] == 1:
                        cnt += 1
                    else:
                        break  # 아니면 중단

                if cnt == K:  # 길이가 정확히 K이면 정답 추가
                    result += 1

    print(f'#{tc} {result}')  # 테스트케이스 번호랑 정답 출력
'''