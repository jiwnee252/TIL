import sys
sys.stdin = open("16268.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(N)
    print(M)
    print(arr)

    # 가로M 세로N


    # dx = [0, 1, 0, 1]  # 시계방향 # 방향별로 더할 값
    # dy = [1, 0, -1, 0]

    for

    # print(f'#{test_case} {result}')