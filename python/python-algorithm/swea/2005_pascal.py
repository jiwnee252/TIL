import sys
sys.stdin = open("2005.txt", "r")

T = int(input())
for test_case in range(1, T+1):

    # print(N//2)
    # N이 5일경우 총 5줄을 출력한다

    N = int(input())  # 각 테스트 케이스.
    print(N)
    pascal = []
    #
    # for i in range(N):
    #     for j in range(i):
    #         pascal[i][j] = 0


    # print(f'#{test_case}')
    # print(result)
