import sys
sys.stdin = open("20396_input.txt", "r")

def flip(init_stone, i, j):
    color = init_stone[i-1]
    for k in range(i-1, i+j-1):
        if k >= len(init_stone):
            break
        init_stone[k] = color
    return init_stone

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    init_stone = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(M)]
    for f in range(M):
        init_stone = flip(init_stone, arr[f][0], arr[f][1])
    print(f'#{test_case} {" ".join(map(str, init_stone))}')
