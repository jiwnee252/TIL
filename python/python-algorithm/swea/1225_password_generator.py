from collections import deque
import sys
sys.stdin = open("1225_password_generator.txt", "r")

for test_case in range(1, 11):
    T = int(input())
    data = deque(list(map(int, input().split())))
    # print(data)
    while data[-1] > 0:
        for i in range(1, 6):
            x = data.popleft() - i
            data.append(x)
            if data[-1] <= 0:
                data[-1] = 0
                break

    print(f'#{T}', *data)