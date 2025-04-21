# 쉬운 거스름돈

import sys
sys.stdin = open('1970.txt', 'r')
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    # print(N)
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0] * 8

    i = 0
    while i < 8:
        change[i] = N // money[i]
        N = N - change[i] * money[i]
        i += 1
    print(f'#{test_case}')
    print(f'{" ".join(map(str, change))}')