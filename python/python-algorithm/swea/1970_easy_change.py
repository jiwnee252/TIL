import sys
sys.stdin = open('1970.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    change_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = []

    for i in range(8):
        if N // change_list[i] != 0:    # 나눠질경우
            change.append(N // change_list[i])    # N을 잔돈으로 나눴을때의 몫
            N = N % change_list[i]   # N에서 N을 잔돈으로 나눴을때의 몫을 뺌 -> 나머지?
        else:
            change.append(0)
    # print(change)

    print(f'#{test_case}\n{" ".join(map(str, change))}')