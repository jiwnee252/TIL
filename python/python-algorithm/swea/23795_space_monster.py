import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 괴물이 arr[i][j]에 있으면.

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(len(arr)):
        for j in range(i):
            # 괴물을 찾을때까지 일단 탐색
            # 괴물은 한마리있음.
            if arr[i][j] == 2:
                # 상하좌우 4칸탐색

