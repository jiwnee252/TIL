from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = deque(list(map(int, input().split())))

    count = 0
    while count < M:
        for i in range(N):
            x = arr.popleft()
            arr.append(x)
            count += 1

            if count == M:
                y = arr.popleft()

    print(f'#{test_case} {y}')