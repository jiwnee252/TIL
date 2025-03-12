import sys
sys.stdin = open("23894_5188_input.txt", "r")

def dp(N, arr):
    # dp 배열 생성 (각 지점까지의 최소 경로 합을 저장)
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = arr[0][0]  # 시작점 초기화

    # 첫 번째 행 초기화 (오른쪽으로만 이동)
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + arr[0][j]

    # 첫 번째 열 초기화 (아래쪽으로만 이동)
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + arr[i][0]

    # 나머지 부분을 채우기 (아래 또는 오른쪽으로 이동)
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + arr[i][j]

    # 목표 지점 (N-1, N-1)까지의 최소 경로 합을 출력
    return dp[N-1][N-1]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{test_case} {dp(N, arr)}')