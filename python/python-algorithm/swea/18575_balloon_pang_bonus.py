import sys
sys.stdin = open("18575.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 풍선을 두번 터트림
    # 한번 터트릴때마다 풍선 배열 초기화
    N = int(input())
    balloon = [list(map(int, input().split())) for _ in range(N)]
    print(balloon)
    print(N)

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]  # 상하좌우

    # 가로
    for i in range(N):
        for j in range(N):
            # 가로 다 터트리고 세로 다 터트린담에 자신을뺌
            pang_sum = balloon[i][j]
            for d in range(4):  # 상하좌우 4방향
                for k in range()
