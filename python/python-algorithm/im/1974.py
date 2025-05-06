# 두개의숫자열
import sys
sys.stdin = open('1974.txt', 'r')
T = int(input())
for test_case in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(sudoku)

    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]   45
    for row in sudoku:
        if sum(row) != 45:
            result = 0



    print(f'{test_case} {result}')