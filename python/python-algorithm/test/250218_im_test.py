import sys
sys.stdin = open('250218_im_test.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # # 최대 이동거리
    # # max(count_list)

    count_list = []
    count = 0  # 이동할때마다
    for i in range(N):
        for j in range(N):
            # ???????????
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                small_list_arr = []  # arr[ni][nj] 중에 젤 작은것
                if 0 <= ni < N and 0 <= nj < N:   # 범위설정
                    if arr[ni][nj] < arr[i][j]:  # 상하좌우 원소가 나보다 작으면
                        small_list_arr.append(arr[ni][nj])
                        # 작은게 여러개 잇으면 그중 젤 작은거
                        if arr[ni][nj] == min(small_list_arr):
                            count += 1  # 카운트 올리고
                            ni, i = i, ni    # 상하좌우 이동.
                            nj, j = j, nj    # ---> 여기까지잘되는데
                            # continue

            count_list.append(count)
    # print(count_list)
    print(f'#{test_case} {max(count_list)}')
    
    # output 6, 10, 8 나와야함