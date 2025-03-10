import sys
sys.stdin = open("20551_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    A, B, C = map(int, input().split())
    if A < B < C:
        print(f'#{test_case} 0')
    elif B < 2 or C < 3:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {A + B - 2 * C + 3}')


