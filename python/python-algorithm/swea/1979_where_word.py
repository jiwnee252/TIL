import sys
sys.stdin = open("1979.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = list(map(int,input().split()))
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    # print(row)

    # row의 요소를 도는데.
    # row의 i-1번째 요소가 0이고, row의 i+k+1번째 요소도 0인데
    # 그사이에는 0이없으면
    # count를 올림
    # 그러면 i-1 >= 0이어야하고 i+k+1 <= N 이어야함
    # N은 5이상 15이하, K는 2이상 N이하

    r_count = 0
    for row in puzzle:
        for i in range(N):
            if i >= 1 and i + K <= N-1:
                if 0 not in row[i:i+K]:
                    if row[i-1] == 0 and row[i+K] == 0: # i+K는 N이하
                        r_count += 1
    # print(r_count)

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

    print(f'#{test_case} {r_count + c_count}')