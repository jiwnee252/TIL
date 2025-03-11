# RGB괴물

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # RGB괴물의수
    area = [list(map(int, input())) for _ in range(10)]
    # 0 괴물없음    1 R괴물 (1칸)   2 G괴물 (2칸)    3 B괴물 (3칸)    4 벽
    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    # 델타..쭉 가다가 123을 만나면 멈춤.
    # 4를 만나도 멈춤.

    safe_area = [[-1] * 10 for _ in range(10)]    # -1이면 안전한곳임

    for i in range(10):
        for j in range(10):
            if area[i][j] != 0:    # 맵을 순회하는데 0이 아니면
                safe_area[i][j] = 1  # 일단 위험하니까 1로 표시해줌
                if area[i][j] == 1:   # 만약 1칸을 비추는 R괴물을 찾으면.
                    # 각방향으로 1칸만 갈거다
                    for d in range(4):
                        ni = i + di[d]
                        nj = j + dj[d]
                        # 상하좌우로 갈건데. 범위 안에 있다면
                        if 0 <= ni < 10 and 0 <= nj < 10:
                            # 1234를만나면 stop, 0이면 safe_area[ni][nj]를 1로바꿔준다
                            if area[ni][nj] == 1 or area[ni][nj] == 2 or area[ni][nj] == 3:
                                safe_area[ni][nj] = 1
                                break

                elif area[i][j] == 2:  # 2칸 g괴물

                    # 2칸가야돼
                    for d in range(4):
                        ni = i + di[d]
                        nj = j + dj[d]
                        # 상하좌우로 갈건데. 범위 안에 있다면
                        if 0 <= ni < 10 and 0 <= nj < 10:
                            # 1234를만나면 stop, 0이면 safe_area[ni][nj]를 1로바꿔준다
                            if area[ni][nj] == 1 or area[ni][nj] == 2 or area[ni][nj] == 3:
                                safe_area[ni][nj] = 1
                                break
                elif area[i][j] == 3:  # 3칸 b괴물

                    # 3칸가야돼
                    for d in range(4):
                        ni = i + di[d]
                        nj = j + dj[d]
                        # 상하좌우로 갈건데. 범위 안에 있다면
                        if 0 <= ni < 10 and 0 <= nj < 10:
                            # 1234를만나면 stop, 0이면 safe_area[ni][nj]를 1로바꿔준다
                            if area[ni][nj] == 1 or area[ni][nj] == 2 or area[ni][nj] == 3:
                                safe_area[ni][nj] = 1
                                break

    for i in range(10):
        for j in range(10):
            if area[i][j] == 4:
                safe_area[i][j] = 1

    safe_count = 0
    for i in range(10):
        for j in range(10):
            if safe_area[i][j] == -1:
                safe_count += 1

    print(f'#{tc} {safe_count}')

'''
2
3
0000000000
0000001000
0000000000
0002000000
0000000000
0000000000
0000003000
0000000000
0000000000
0000000000
8
0000000000
0020000000
0000030000
0000000200
0010000000
0000000000
0000200000
0304000030
0400000010
0000000000

'''


# 마저풀기