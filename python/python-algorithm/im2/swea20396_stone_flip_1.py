import sys
sys.stdin = open("20396.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 돌의 개수, M: 뒤집기 명령의 개수
    arr = list(map(int, input().split()))  # 초기 돌 상태 (0 또는 1)

    for _ in range(M):  # M번 뒤집기 명령 수행
        i, j = map(int, input().split())  # i: 기준 위치, j: 뒤집을 돌의 개수
        color = arr[i - 1]  # 기준 위치에 있는 돌의 현재 상태 저장 (0 또는 1)

        # 기준 위치부터 j개의 돌을 같은 상태로 뒤집기
        for k in range(i - 1, i + j - 1):
            if k >= N:  # 돌의 범위를 벗어나면 중지
                break
            arr[k] = color  # 해당 위치의 돌을 기준 돌 상태로 변경 (뒤집기)

    print(f'#{tc}', *arr)
