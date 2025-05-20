import sys
sys.stdin = open("20739.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    # 가로로 연속한 1의 개수
    for i in range(N):
        cnt = 0             # 행이 바뀌면 1의 개수 초기화
        for j in range(M):
            if arr[i][j]:
                cnt += 1
                if max_v < cnt:
                    max_v = cnt
            else:
                cnt = 0
    # 세로로 연속한 1의 개수
    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j]:
                cnt += 1
                if max_v < cnt:
                    max_v = cnt
            else:
                cnt = 0
    if max_v == 1:  # 노이즈만 있는 경우
        max_v = 0
    print(f'#{tc} {max_v}')