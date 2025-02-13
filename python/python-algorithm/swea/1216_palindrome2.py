import sys
sys.stdin = open("1216.txt", "r")
for test_case in range(1, 11):
    T = int(input())
    # 100x100회문  # 가장긴회문의길이를구하라.
    p = [list(map(str, input())) for _ in range(100)]

    # N = 1  # 가로 회문의 길이  # 1부터올려줄거임   # 100이하
    max_N = 1    # 최대회문의길이 1이라가정하고
    for row_list in p:                   # 가로에서
        for i in range(100):          # i+N <= 100이어야하므로..   # 0행부터 100-N행까지검사하는데
            for N in range(1, 101):    # (각행마다)회문의길이 1부터 100까지 검사하는데
                if i + N <= 100:
                    word = row_list[i:i + N]  # 회문인지검사하는법
                    if word == word[::-1]:              # 만약에회문이면
                        max_N = max(max_N, N)              # 최대회문의길이를업데이트함
    # print(max_N)

    # M = 1
    max_M = 1

    for col in range(len(p)):    # 세로
        col_list = []
        for row in p:
            col_list.append(row[col])
        # print(col_list)
        # for column in col_list:
        for j in range(100):
            for M in range(1, 101):
                if j + M <= 100:
                    c_word = col_list[j:j+M]
                    if c_word == c_word[::-1]:
                        max_M = max(max_M, M)
    # print(max_M)

    result = max(max_N, max_M)

    print(f'#{T} {result}')