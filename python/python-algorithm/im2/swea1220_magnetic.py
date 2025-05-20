import sys
sys.stdin = open("1220.txt", "r")

T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = 0

    for c in range(100):
        state = 0               # n극 존재여부 기록
        for r in range(100):

            if arr[r][c] == 1:  # 아래로 향하는 n극
                state = 1

            if state == 1 and arr[r][c] == 2:   # 교착상태 발생
                result += 1
                state = 0

    print(f'#{tc} {result}')