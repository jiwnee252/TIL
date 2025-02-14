import sys
sys.stdin = open("4615.txt", "r")

T = int(input())
for test_case in (1, T+1):
    N, M = map(int, input().split())
    print(N, M) # N: 보드의 한 변의 길이. 4, 6, 8 중 하나   /  M : 플레이어가 돌을 놓는 횟수
    matrix = [list(input().split()) for _ in range(M)]
    print(matrix)

    #