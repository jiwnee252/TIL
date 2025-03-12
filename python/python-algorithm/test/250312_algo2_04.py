T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    start = [arr[0], arr[1]]
    end = [arr[2], arr[3]]
    arr2 = [list(map(int, input().split())) for _ in range(N)]
    # print(f'왼쪽위, 오른쪽아래:{arr}')
    # print(f'마당:{arr2}')
    # print(start, end)

    # 평탄화 영역의 높이 값의 합
    area_count = 0  # 영역의 칸수
    height_sum = 0
    average_ = 0
    flatten_count = []
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            area_count += 1
            height_sum += arr2[i][j]
            average_ = height_sum // area_count
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            flatten_count.append(abs(arr2[i][j] - average_))
    # print(average_)
    # print(sum(flatten_count))
    print(f'#{test_case} {sum(flatten_count)}')
