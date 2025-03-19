# bfs?
from collections import deque

def min_calc(n, m):
    queue = deque([n])     # 현재값
    count = 0              # 연산한 횟수
    visited = set()
    visited.add(n)

    while queue:
        # 현재값 cur
        cur = queue.popleft()
        if cur == m:
            return count

            calc_ = [cur + 1, cur - 1, cur * 2, cur - 10]   # 가능한 다음값.
            for calc in calc_:  # 가능한 다음값 하나씩 순회하면서
                if 1 <= calc <= 1000000 and calc not in visited:   # 만약 연산의 중간결과가 백만 이하이고, 이미 만난 숫자가 아니면
                    queue.append(calc)  # 큐에 다음값을 넣는다.
                    visited.add(calc)
        count += 1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    answer = min_calc(N, M)
    print(f'#{test_case} {answer}')