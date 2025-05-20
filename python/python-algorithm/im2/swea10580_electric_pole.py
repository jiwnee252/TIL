import sys
sys.stdin = open("10580.txt", "r")

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 전선 개수

    ab = [list(map(int, input().split())) for _ in range(N)]

    ab.sort()

    cnt = 0     # 교차점 수
    for i in range(1, N):
        for j in range(i):  # A는 더 낮지만 B가 더 높은 경우 교차
            if ab[j][1] > ab[i][1]:
                cnt += 1

    print(f'#{tc} {cnt}')