T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # RGB 괴물의 수
    matrix = [list(map(int, input())) for _ in range(10)]
    # 0 괴물없음 1 R괴물(1칸) 2 G괴물(2칸) 3 B괴물(3칸) 4 벽
    print(N)
    print(matrix)

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]


    # print(f'#{test_case} {result}')
