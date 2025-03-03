from collections import deque
import sys
sys.stdin = open("1860_jinki.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    # N 붕어빵 먹을수 잇는 사람수 M m초동안 K k개만들수잇음
    arrive_time = list(map(int, input().split()))   # 각 사람이 언제 도착하는지


    print(f'#{test_case} {bread(N, M, K, arrive_time)}')