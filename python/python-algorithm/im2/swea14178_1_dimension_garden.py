import sys
sys.stdin = open("14178.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N , D = map(int, input().split())
    X = 2 * D + 1           # 1개의 분무기가 동작하는 구간
    print(f'#{tc} {N//X +  (N%X>0)}')   # + (N%X > 0) 은 남는 영역이 있는 경우 분무기 수를 +1 하는 연산