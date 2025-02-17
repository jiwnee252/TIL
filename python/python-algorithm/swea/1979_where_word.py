import sys
sys.stdin = open("1979.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):   # N*N 사이즈 퍼즐 # K는 단어의 길이
    N, K = list(map(int, input().split()))
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    puzzle2 = list(map(list, zip(*puzzle))) # 세로

    # count1 = 0
    ans = 0
    count2 = 0

    for row in puzzle:
        print(row)
        # if 0 not in row[i:i+K] and row[i-1] == 0 and row[i+K+1] == 0
    # print(f'#{test_case} {count_puzzle1 + count_puzzle2}')
'''
    
    r_count = 0
    for row in puzzle:
        # print(row)
        for i in range(N):
            pass

    # print(r_count)
    # print("여기까지")
    c_count = 0
    for row in range(N):
        col = []
        for i in puzzle:
            col.append(i[row])
        # print(col)
        for j in range(N):
            if j >= 1 and j + K <= N-1:
                if 0 not in col[j:j+K]:
                    if col[j-1] == 0 and col[j+K] == 0 :
                        c_count += 1
    # print(c_count)
    # print(f'#{test_case} {r_count + c_count}')
'''