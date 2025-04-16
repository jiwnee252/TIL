# 6485 삼성시의 버스노선

import sys
sys.stdin = open('6485.txt', 'r')
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ai_bi_ = [list(map(int, input().split())) for _ in range(N)]
    ai_ = ai_bi_[0]
    bi_ = ai_bi_[1]
    print(ai_, bi_)
    P = int(input())
    cj_ = [int(input()) for _ in range(N)]
    # print(N, ab, P, c)

    # j번째 정수는 Cj번 버스 정류장을 지나는 버스 노선의 개수
    print(f'#{test_case}')


    # 버스정류장이 1부터 5000까지 총 5000개가 있음
    # 버스노선은 N개가 있음
    # i번째 버스노선은 번호가 Ai 이상임
    # 예를들어 1번째 버스노선의 번호는 A1 이상 B1 이하
    # 30번째 버스노선의 번호는 A30 이상 B30 이하
    # P개의 버스 정류장에 대해 각 정류장에 몇개의 버스노선이 다니는지 구하라
    # 예를들어 P가 5라고하면, 5개의 버스정류장 각각에 몇개의 버스노선이 다니는가?
    # C1, C2, C3, C4, C5에 몇개의 버스노선이 다니냐는것임.
    # 문제가뭔소린지몰르겟음.......