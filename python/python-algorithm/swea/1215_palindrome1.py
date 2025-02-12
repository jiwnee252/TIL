import sys
sys.stdin = open("1215.txt", "r")

# T = int(input())
for test_case in range(1, 11):
    N = int(input())    # 찾아야 하는 회문의 길이
    p = [list(map(str, input())) for _ in range(8)]
    print(N)
    count = 0  # 회문찾을때마다 증가  # 가로일때찾고 세로일때찾아서 더해주기

    for row_list in p: # 가로일때.
        print(row_list)
        for x in range(len(row_list)-N):
            if row_list[x:x+N] == row_list[x+N-1:x-1:-1]:
                count += 1
    print(count)

    for col in range(len(p)):        # 세로일때
        col_list = []
        for row in p:
            col_list.append(row[col])
        print(col_list)
        for y in range(len(col_list) - N):
            if col_list[y : y+N] == col_list[y+N-1 : y-1 : -1]:
                count += 1

    print(count)

    print(f'#{test_case} {count}')


