import sys
sys.stdin = open("1959.txt", 'r')

T = int(input())
for tc in range(1, T+1):
    result = []
    N = int(input())
    P = int(input())
    all_bus = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            all_bus[i] += 1
    for i in range(P):
        p1 = int(input())
        result.append(all_bus[p1])
    print(f'#{tc}, *result')