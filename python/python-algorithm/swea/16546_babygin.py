import sys
sys.stdin = open("16546.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = list(map(int, input()))
    result = 'false'
    # N_sort = sorted(N)
    # # print(N_sort)

    print(f'#{test_case} {result}')