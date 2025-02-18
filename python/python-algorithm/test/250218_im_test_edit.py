import sys
sys.stdin = open('250218_im_test.txt', 'r')
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    max_count = 0  # 최대이동거리
    
    for i in range(N):
        for j in range(N):
    
            count = 1    # 나포함 1부터 카운트
            ni, nj = i, j  # 시작 위치

            while True:
                small_arr = []   # 나보다작은수(이동가능한칸) 리스트 초기화

                for d in range(4):  # 상하좌우 계산
                    new_ni = ni + di[d]
                    new_nj = nj + dj[d]

                    if 0 <= new_ni < N and 0 <= new_nj < N:     # 범위안에있고
                        if arr[new_ni][new_nj] < arr[ni][nj]:       # 현재값보다 작으면
                            small_arr.append((arr[new_ni][new_nj], new_ni, new_nj))      # small_list_arr에 해당 숫자, 좌표 추가

                if small_arr:          # 나보다 작은값이 존재하면
                    small_arr.sort()  # 정렬 (0번째인덱스 기준)
                    smallest_value, smallest_i, smallest_j = small_arr[0]  # 제일 작은 값과 좌표
                    ni, nj = smallest_i, smallest_j  # ni nj에 제일 작은 좌표 할당
                    count += 1  # 이동
                else:           # 나보다 작은값이 없으면 break.
                    break

            max_count = max(max_count, count)   # tc 최대이동거리 갱신

    print(f'#{test_case} {max_count}')
