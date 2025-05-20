import sys
sys.stdin = open("22407.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    m = [[0] * 10 for i in range(10)]
    for _ in range(2):  # 2개의 영역
        r1, c1, r2, c2 = map(int, input().split())  # 좌상단, 우하단
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                m[i][j] += 1  # 칠하기

    r1 = c1 = r2 = c2 = -1
    for i in range(10):
        for j in range(10):
            if m[i][j] == 2:  # 보라색
                if r1 == -1:  # 좌상단
                    r1, c1 = i, j
                r2, c2 = i, j  # 마지막에 기록된 인덱스가 우하단
    w = h = 0
    if r1 != -1:
        h = r2 - r1 + 1
        w = c2 - c1 + 1
    print(f'#{tc} {w} {h}')
