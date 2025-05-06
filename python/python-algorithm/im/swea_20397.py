# 20397 돌 뒤집기 게임 2

import sys
sys.stdin = open("20397.txt", 'r')
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    stone = list(map(int, input().split()))
    IJ = [list(map(int, input().split())) for _ in range(M)]
    print(f'#{test_case}')

    # print(stone)
    print(IJ)
