import sys
sys.stdin = open("1961_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)

    i= len(arr)  # 행의 좌표
    j= len(arr[0])  # 열의 좌표
    # print(i, j)

    for i in range(N):
        for j in range(N):




        print(arr)
    # 시계 방향으로 90도 회전
    # arr_90

    # 시계 방향으로 180도 회전
    # arr_180

    # 시계 방향으로 270도 회전
    # arr_270

    # print(f'#{test_case} {result}')

    # 1 2 3       7 4 1       9 8 7       3 6 9
    # 4 5 6       8 5 2       6 5 4       2 5 8
    # 7 8 9       9 6 3       3 2 1       1 4 7