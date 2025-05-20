import sys
sys.stdin = open('13428.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    N = len(arr)

    M = int(''.join(arr))
    max_v = M
    min_v = M  # int(1e9)

    for i in range(N-1):
        for j in range(i, N): # j==i 교환하지 않는 경우
            if i==0 and arr[j] == '0': # 0이 앞으로 오는 경우 제외
                continue
            arr[i], arr[j] = arr[j], arr[i] # 자리 교환
            M = int(''.join(arr))
            if max_v < M:
                max_v = M
            if min_v > M:
                min_v = M
            arr[i], arr[j] = arr[j], arr[i]  # 원래 위치로

    print(f'#{tc} {min_v} {max_v}')