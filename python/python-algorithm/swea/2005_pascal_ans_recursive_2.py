import sys
sys.stdin = open('input.txt')

# row[n] => [1] + row[n-1] + [1]
# row[n-1] 을 2개씩 묶어서 더한 값으로 푸는 로직이 추가되어야 한다.
def pascal_triangle(n):
    # 첫 번째 행은 무조건 [1]
    if n == 1:
        return [1]

    # 윗 줄의 리스트를 가져오도록 재귀적으로 시킨다.
    prev_row = pascal_triangle(n-1)

    # 새로운 행의 시작은 항상 [1]
    new_row = [1]

    # prev_row 리스트를 순회하면서 2개씩 묶어서 더한 값을 new_row 에 추가하면 된다.
    for i in range(len(prev_row) - 1):
        new_row.append(prev_row[i] + prev_row[i+1])

    # 마지막은 항상 1
    new_row.append(1)

    return new_row




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')

    # 각 행에 대해서 재귀함수를 실행합니다.
    for i in range(1, N + 1):
        row = pascal_triangle(i)
