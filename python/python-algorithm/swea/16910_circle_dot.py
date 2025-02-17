import sys
sys.stdin = open("16910.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    # 반지름 N인 원 안에 포함되는 격자점의 개수

    # print(f'#{test_case} {result}')