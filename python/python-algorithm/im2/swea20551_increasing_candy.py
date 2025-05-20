import sys
sys.stdin = open("20551.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    result = 0

    # 수열이 증가해야 하므로 B는 최소 2, C는 최소 3이어야 의미가 있음
    if B < 2 or C < 3:
        result = -1  # 조건을 만족할 수 없으면 -1 출력
    else:
        # B가 C보다 크거나 같다면 조정 필요
        if B >= C:
            result += (B - C + 1)
            B -= (B - C + 1)

            # A가 B보다 크거나 같다면 다시 조정
        if A >= B:
            result += (A - B + 1)

    print(f'#{tc} {result}')
