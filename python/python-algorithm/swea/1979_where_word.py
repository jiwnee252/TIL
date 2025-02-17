import sys
sys.stdin = open("1979.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):   # N*N 사이즈 퍼즐 # K는 단어의 길이
    N, K = list(map(int, input().split()))
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    puzzle2 = list(map(list, zip(*puzzle)))     # 세로

    ans1 = 0
    ans2 = 0
    for row in puzzle:
        count1 = 0
        for i in range(N):
            if row[i] == 1:
                count1 += 1
            if row[i] == 0 or i == N-1:
                if count1 == K:
                    ans1 += 1
                    count1 = 0
                else:
                    count1 = 0
    print(ans1)
    for col in puzzle2:
        count2 = 0
        for j in range(N):
            if col[j] == 1:
                count2 += 1
            if col[j] == 0 or j == N-1:
                if count2 == K:
                    ans2 += 1
                    count2 = 0
                else:
                    count2 = 0

    print(ans2)

    print(f'#{test_case} {ans1 + ans2}')