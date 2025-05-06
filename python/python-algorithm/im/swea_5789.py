# 5789 현주의 상자 바꾸기
import sys
sys.stdin = open("5789.txt", 'r')
T = int(input())
for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0] * N

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        # print(L, R)
        for box in range(L-1, R):
            boxes[box] = i

    # print(boxes)
    print(f'#{test_case} {" ".join(map(str, boxes))}')
