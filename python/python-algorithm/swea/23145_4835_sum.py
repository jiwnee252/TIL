import sys
sys.stdin = open("23145_4835_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # print(N, M)
    a = list(map(int, input().split()))
    # print(a)

    m_sum_list = []

    for i in range(N-M+1):  # N 정수의 개수 # M 구간의 개수
        current_sum = 0
        for j in range(M):
            current_sum += a[i + j]
        m_sum_list.append(current_sum)

    result = max(m_sum_list) - min(m_sum_list)
    print(f'#{test_case} {result}')