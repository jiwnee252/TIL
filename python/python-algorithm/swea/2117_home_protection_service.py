import sys
sys.stdin = open("2117_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())    # N 도시의크기 M 하나의집이 지불할수있는 비용
    arr = [list(map(int, input().split())) for _ in range(N)]
    # op_fee 운영비 K 서비스 영역의 크기
    K = 0
    op_fee = K * K + (K - 1) * (K - 1)
    # 보안회사의 이익 = 서비스제공받는집수익 - 운영비용
    home = 0       # 서비스제공받는 집
    profit = home * M - op_fee