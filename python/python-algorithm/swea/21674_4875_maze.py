import sys
sys.stdin = open("21674_4875_input.txt", "r")

def find_maze_path(arr, n):
    stack = []
    for i in range(n):
        for j in range(n):
            while True:
                if arr[i][j] == 3:   # 3부터 내려가서 2를 찾기
                    if arr[i-1][j] == 0 or arr[i+1][j] == 0 or arr[i][j+1] == 0:
                        stack.append([i, j])
                        if stack:
                            i = stack.pop()[0]
                            j = stack.pop()[1]
                            if arr[i-1][j] == 2 or arr[i+1][j] == 2 or arr[i][j+1] == 2:
                                return 1
                else: return 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # print(N)
    # print(maze)

    result = find_maze_path(maze, N)
    print(f'#{test_case} {result}')
