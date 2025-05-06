import sys
sys.stdin = open("12712.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0  # 최대 퇴치 파리수
    for i in range(N):  # 모든 원소에 스프레이...
        for j in range(N):
            s = arr[i][j]  # 스프레이 중심
            # + 로 뿌려지는 경우
            di = [0, 1, 0, -1]
            dj = [1, 0, -1, 0]
            for k in range(4):  # k 방향
                for z in range(1, M):  # 중심에서의 거리
                    ni, nj = i + di[k] * z, j + dj[k] * z
                    if 0 <= ni                         s += arr[ni][nj]
            if max_v < s:  # 최대값과 비교
                max_v = s
            # X 방향으로 뿌리는 경우
            di = [1, 1, -1, -1]
            dj = [1, -1, -1, 1]
            s = arr[i][j]  # 스프레이 중심
            for k in range(4):  # k 방향
                for z in range(1, M):  # 중심에서의 거리
                    ni, nj = i + di[k] * z, j + dj[k] * z
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
            if max_v < s:
                max_v = s
    print(f'#{tc} {max_v}')
