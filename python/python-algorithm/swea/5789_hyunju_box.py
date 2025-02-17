import sys
sys.stdin = open("5789.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, Q = map(int, input().split())
    box = [0] * N

    for i in range(Q):  # 0~Q-1
        L, Q = map(int, input().split())
        for j in range(L-1, Q):
            box[j] = i + 1


    print(f'#{test_case} {" ".join(map(str, box))}')