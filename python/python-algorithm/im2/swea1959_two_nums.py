import sys
sys.stdin = open("1959.txt", "r")
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    if N < M:
        long = Bj
        short = Ai
        count = M - N + 1
    else:
        long = Ai
        short = Bj
        count = N - M + 1

    max_value = 0
    for i in range(count):
        total = 0
        for idx in range(len(short)):
            total += short[idx] * long[idx + i]
        if max_value < total:
            max_value = total

    print(f'#{tc} {max_value}')

