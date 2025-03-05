T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    player = list(map(int, input().split()))
    # 정렬
    player.sort()
    max_members = 0
    i = 0
    for j in range(N):
        while player[j] - player[i] > K:
            i += 1
        max_members = max(max_members, j - i + 1)
    print(f'#{tc} {max_members}')
