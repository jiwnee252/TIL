import sys
sys.stdin = open("11039.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 1

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:

                r_cnt = 1
                c_cnt = 1
                # 가로 순회
                while j + 1 <= N - 1 and arr[i][j + 1] == 1:
                    r_cnt += 1
                    j += 1
                # 세로 순회
                while i + 1 <= N - 1 and arr[i + 1][j] == 1:
                    c_cnt += 1
                    i += 1
                if max_v < r_cnt * c_cnt:
                    max_v = r_cnt * c_cnt

    print(f'#{tc} {max_v}')