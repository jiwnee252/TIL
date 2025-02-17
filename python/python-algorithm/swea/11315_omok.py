import sys
sys.stdin = open("11315.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    # print(N)
    stone = [list(map(str, input())) for _ in range(N)] # 가로
    # print(stone)
    stone2 = list(map(list, zip(*stone)))   # 세로
    # print(stone2)

    result = 0
    # 가로
    for row in stone:
        sum1 = 0
        for i in range(N):
            if row[i] == 'o':
                sum1 += 1
            if row[i] == '.' or i == N-1:
                if sum1 == 5:
                    result = 'YES'
                else:
                    result = "NO"
                sum1 = 0
    # 세로
    for row in stone2:
        sum2 = 0
        for i in range(N):
            if row[i] == 'o':
                sum2 += 1
            if row[i] == '.' or i == N-1: # 끝까지
                if sum2 == 5:
                    result = 'YES'
                else:
                    result = "NO"
                sum2 = 0

    # 대각선
    for i in range(N):
        for j in range(N):


    print(f'#{test_case} {result}')