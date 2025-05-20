import sys
sys.stdin = open('18575.txt')

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # N개의 행의 합
    row_total_list = []
    # N개의 열의 합
    col_total_list = []

    for row in range(N):
        total = 0
        for col in range(N):
            total += arr[row][col]   # 행의 합

        row_total_list.append(total)

    for col in range(N):
        total = 0
        for row in range(N):
            total += arr[row][col]

        col_total_list.append(total)

    # print(row_total_list)   # N개의 행
    # print(col_total_list)   # N개의 열의 합
    # 무작정 max(row_total_list) , max(col_total_list) 하게 되었을 때
    # 풍선 값을 고려하지 않았기에 오답이 나올 가능성이 큼!!!
    # 행의합 + 열의합 - (위치의 값)   전체를 계산해서 최대, 최소를 확인

    max_value = 0
    min_value = 99999
    for i in range(N):  # i 인덱스의 행의 합
        for j in range(N):  # j 인덱스의 열의합
            # 행의합 + 열의합 - (위치의 값)
            total = row_total_list[i] + col_total_list[j] - arr[i][j]
            # total 이 최대인 것과 최소 인 것을 찾아서 차이를 구하면 됨
            if max_value < total:
                max_value = total

            if min_value > total:
                min_value = total

    # 보너스 점수 max - min
    print(f'#{tc} {max_value - min_value}')