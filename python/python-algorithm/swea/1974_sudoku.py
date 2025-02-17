import sys
sys.stdin = open("1974.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(T)
    print(sudoku)
    for row in sudoku:
        print(*row)

    # 가로
    for row in sudoku:
        for i in range(9):
           if row[i] != row
    # 세로
    # 격자

    result = 0

    print(f'#{test_case} {result}')
