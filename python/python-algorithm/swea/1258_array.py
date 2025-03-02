T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_list = []
    arr_count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:  # 0이 아닌곳을 발견하면
                arr[i][j] = 0 # 0으로 바꿔서 탐색완료체크
                arr_count += 1
                width = 1
                height = 1
                while arr[i + height][j] != 0 and i + height < n:
                    arr[i + height][j] = 0
                    height += 1
                while arr[i][j + width] != 0 and j + width < n:
                    arr[i][j + width] = 0
                    width += 1
                arr_list.append([width * height, width, height])
                for a in range(i, i + height):
                    for b in range(j, j + width):
                        arr[a][b] = 0



    arr_list.sort(key=lambda x: (x[0], x[2], x[1]))
    # print(arr_list)
    # print(arr_count)

    print(f'#{test_case} {arr_count} {" ".join(f"{x[2]} {x[1]}" for x in arr_list)}')

