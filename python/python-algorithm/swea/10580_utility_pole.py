import sys
sys.stdin = open("10580_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][0] < arr[j][0] and arr[i][1] > arr[j][1]:
                count += 1
    print(f'#{test_case} {count}')
