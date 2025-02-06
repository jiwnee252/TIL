#최대값이 아니라 최대값 위치가 필요한거임

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    # 최대값 위치에서 1빼기 최소값 위치에서 1더하기를 N번
    for _ in range(N):
        max_idx = 0
        min_idx = 0
        for i in range(100) :
            if data[i] > data[max_idx]:
                max_idx = i
            if data[i] < data[min_idx]:
                min_idx = i
        data[max_idx] -= 1
        data[min_idx] += 1
    # 덤프 끝나고 한번더 찾아서
    max_idx = 0
    min_idx = 0
    for i in range(100):
        if data[i] > data[max_idx]:
            max_idx = i
        if data[i] < data[min_idx]:
            min_idx = i

print(f'#{tc} {data[max_idx]-data[min_idx]}')