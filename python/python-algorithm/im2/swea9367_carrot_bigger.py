import sys
sys.stdin = open("9367.txt", "r")
T = int(input())
for tc in range(1, T+1):
    cnt = 1     # 연속으로 커지지 않는 경우 구간의 최소 길이는 1
    max_v = 1
    N = int(input())
    a = list(map(int, input().split()))
    for i in range(1, N):
        if a[i-1] < a[i]:   # 커지는 구간
            cnt += 1
            if max_v < cnt:
                max_v = cnt
           else:
            cnt = 1
    print(f'#{tc} {max_v}')