import sys
sys.stdin = open("23795.txt", "r")

def f(N):   # 광선 표시
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:  # 우주괴물
                for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                    for k in range(1, N):
                        ni, nj = i+di*k, j+dj*k
                        if 0<=ni                            arr[ni][nj] = 1
                        else:
                            break
                return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    f(N)
    ans = 0                     # 안전구역 개수
    for i in range(N):          # 안전구역 찾기
        for j in range(N):
            if arr[i][j] == 0:
                ans += 1
    print(f'#{tc} {ans}')