# bfs?
from collections import deque

def min_calc(n, m):
    queue = deque([(n, 0)])  # (현재값, 연산 횟수)
    visited = set([n])

    while queue:
        cur, count = queue.popleft()

        if cur == m:
            return count

        calc_ = [cur + 1, cur - 1, cur * 2, cur - 10]

        for calc in calc_:
            if 1 <= calc <= 1000000 and calc not in visited:
                queue.append((calc, count + 1))
                visited.add(calc)

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    answer = min_calc(N, M)
    print(f'#{test_case} {answer}')