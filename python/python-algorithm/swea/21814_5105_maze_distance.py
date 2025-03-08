import sys
sys.stdin = open("21814_5105_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    print(maze)

    # print(f'#{tc} {result}')
    # 0 통로 1 벽 2 출발 3 도착
    print()