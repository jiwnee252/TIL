import sys

sys.stdin = open('../../../../../Downloads/input.txt')

for _ in range(10):
    tc = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 현재까지의 각행/각열/대각선들 중에서 최대값을 저장하는 변수
    result = 0

    for i in range(N):  # 행을 의미하는 코드
        tmp = 0  # 각 행별 최대값을 저장하는 임시 변수
        for j in range(N):  # 열을 의미하는 코드 ( 열을 이동시키면서 값을 누적시킨다 )
            tmp += arr[i][j]
        result = max(tmp, result)  # tmp랑 result 둘 중 최대값, 큰 값이 빠져나와서 result에 할당되는 코드입니다.

    # 각 열의 최대값
    for i in range(N):  # 열을 의미하는 코드
        tmp = 0
        for j in range(N):  # 행을 의미하는 코드
            tmp += arr[j][i]
        result = max(tmp, result)

    # 주 대각선의 합 (좌상 -> 우하단 )
    tmp = 0
    # for i in range(N):
    #     for j in range(N):
    #         if i == j:  # 두 인덱스가 서로 같은 경우
    #             tmp += arr[i][j]
    # result = max(tmp, result)

    for i in range(N):
        tmp += arr[i][i]
    result = max(tmp, result)

    # 부 대각선의 합 ( 우상단 -> 좌하단 )
    tmp = 0
    # for i in range(N):
    #     for j in range(N):
    #         if i == N - 1 - j:  # 두 인덱스가 적절한 같은 값?
    #             tmp += arr[i][j]
    # result = max(tmp, result)

    for i in range(N):
        tmp += arr[i][N-1-i]
    result = max(tmp, result)

    print(f'#{tc} {result}')
