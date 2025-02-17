import sys
sys.stdin = open("algo1_sample_in.txt", "r")
T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))  # N 팀원 # M 명령의 횟수
    st = list(map(int, input().split()))

    for _ in range(M):
        a, b, c = list(map(int, input().split()))
        # print(a)
        # print(b)
        # print(c)
        for i in range(b, b+c):
            if i <= N:
                if st[i - 1] == 1:
                    st[i - 1] = 0
                else:
                    st[i - 1] = 1

    print(f'#{test_case} {st}')


