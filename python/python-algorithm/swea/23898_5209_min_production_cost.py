T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    print(cost)