import sys
sys.stdin = open("12741.txt", "r")

T = int(input())
ans = []
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    on = max(A, C)          # A, C 중 나중에 켜지는 전구 기준
    off = min(B, D)         # B, D 중 먼저 꺼지는 전구 기준
    ans.append( off - on if off >= on else 0)   # 실제 켜진 시간이 있는 경우가 아니면 0

for i in range(T):              # 출력시간을 줄이기 위해 답을 모아서 출력
    print(f'#{i+1} {ans[i]}')