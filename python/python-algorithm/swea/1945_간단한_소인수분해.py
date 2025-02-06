import sys
sys.stdin = open("1945_간단한_소인수분해.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    # N을 2로 계속 나눔..언제까지?
    # N % 2 !== 0 이 될때까지..
    # 그담에 3 5 7 11 반복

    i = 0  # 나누는횟수
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_e = 0

    while i <= N :
        if (N % 2) != 0 :
            break
        else :
            N = N / 2
            count_a += 1

    while i <= N :
        if (N % 3) != 0 :
            break
        else :
            N = N / 3
            count_b += 1

    while i <= N :
        if (N % 5) != 0 :
            break
        else :
            N = N / 5
            count_c += 1

    while i <= N :
        if (N % 7) != 0 :
            break
        else :
            N = N / 7
            count_d += 1

    while i <= N :
        if (N % 11) != 0 :
            break
        else :
            N = N / 11
            count_e += 1

    print(f'#{test_case} {count_a} {count_b} {count_c} {count_d} {count_e}')