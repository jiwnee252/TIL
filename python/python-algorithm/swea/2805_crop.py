import sys
sys.stdin = open("2805.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    crop_value = [list(map(int, input())) for _ in range(N)]    # 농작물 가치 리스트
    crop_value_sum = sum(map(sum, crop_value))    # 농장의 모든 농작물 가치의 합

    half_sum = []   # 각 줄의 합
    half = 0    # 가운데 줄의 합

    for i in range(N):
        if i < N//2:        # 가운데줄 기준으로 위의합
            for j in range(N//2 - i, N//2 + i + 1):
                half_sum.append(crop_value[i][j])
        elif i == N//2:
            for j in range(N):      # 가운데줄의합
                half += crop_value[i][j]
        else:                           # 가운데줄 기준으로 아래의합
            for j in range(N//2 - (N-i-1), N//2 + (N-i-1) + 1):
                half_sum.append(crop_value[i][j])

    profit = sum(half_sum) + half
    print(f'#{test_case} {profit}')
