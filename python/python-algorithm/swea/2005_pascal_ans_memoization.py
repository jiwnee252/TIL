import sys

sys.stdin = open('input.txt')


def pascal_triangle(n, memo={}):
    if n == 1:
        return [1]

    if n in memo:
        return memo[n]

    prev_row = pascal_triangle(n - 1, memo)
    new_row = [1]

    for i in range(len(prev_row) - 1):
        new_row.append(prev_row[i] + prev_row[i + 1])

    new_row.append(1)
    memo[n] = new_row
    return new_row


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')

    memo = {}
    for i in range(1, N + 1):
        row = pascal_triangle(i, memo)
        print(' '.join(map(str, row)))
