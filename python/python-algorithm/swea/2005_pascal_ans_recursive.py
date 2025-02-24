import sys

sys.stdin = open('input.txt')


# row, col 이 주어졌을 때, 이전(윗줄)에 있는 row와 col을 재귀적으로 구하는 재귀함수
def pascal_triangle(row, col):
    # 종료 조건
    # col == 0 => 1열
    if col == 0:
        return 1

    # 대각선일 때는 무조건 1
    if row == col:
        return 1

    # 범위가 줄어드는 코드
    return pascal_triangle(row-1, col-1) + pascal_triangle(row-1, col)



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')

    # 파스칼 삼각형의 모든 (i, j)에 접근하기 위한 for 문이에요
    for i in range(N):
        row = []
        for j in range(i + 1):
            row.append(str(pascal_triangle(i, j)))
        print(' '.join(row))



