import sys
sys.stdin = open("3456.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    a, b, c = map(int, input().split())

    ans = 0
    if a == b:
        ans = c
    elif a == c:
        ans = b
    else:           # b == c
        ans = a
    print(f'#{tc} {ans}')