import sys
sys.stdin = open("1959.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    print(N, M) # N = len(Ai), M = len(Bj)
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    print(Ai)
    print(Bj)
    sum = 0
    if M > N:  # Bj가 Ai 보다 길다
        for i in range(N):

    elif M == N:  # Bj와 Ai가 같다
            sum += Ai[i] * Bj[i]
    else:  # Bj가 Ai보다 짧다
        for i in range(M):
            

    # print(f'#{test_case} {result}')