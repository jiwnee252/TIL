import sys
sys.stdin = open("20397_input.txt", "r")

def flip(stone, arr):
    for k in arr:
        i = k[0]
        j = k[1]
        for h in range(1, j+1):
            if i-j >= 0 and i+j < N:
                if stone[i-h] == 1 and stone[i+h] == 1:
                    stone[i-h] = 0
                    stone[i+h] = 0
                elif stone[i-h] == 0 and stone[i+h] == 0:
                    stone[i-h] = 1
                    stone[i+h] = 1
    return stone

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    stone = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(M)]

    p = 1
    while p <= M:
        stone = flip(stone, arr)
        p += 1


    print(f'#{test_case} {stone}')
