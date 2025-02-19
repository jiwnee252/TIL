import sys
sys.stdin = open('21647_4869.txt', 'r')


# print(N)

# 세로는 20, 가로는 N 인 직사각형을 채워줘야 하는데.

# 일단 가로세로 스택을 만들어준 다음에    # 종이 한번 붙일때마다 가로세로 스택에 길이 넣어주고 count 올려줌.

# while True: 가로에 20 또는 10을 계속 넣어줄거임

# ex1)
# 가로에 20을 넣음
# 세로에도 20을 넣음
# 카운트 1 올림

# ex2)
# 가로에 20을 넣음
# 세로에 10을 넣음
# 카운트 1 올림

# 그러면 10만큼 공간이 남아버리니깐
# -> 다음엔 세로에 10넣어주고 가로에 20넣어줌
# 카운트 1 올림

# ex3)
# 가로에 10을 넣음
# 세로에 20을 넣음
# 카운트 1 올림

# if sum(sero_stack) == 20 일때 (세로에 빈공간이 없을때)
# 만약 가로스택에 있는요소를 다 더했는데 N이 되면 ( sum[garo_stack] == N 이면) break하고
# 그때까지 스택에 넣은 횟수 count = 정답


def paper(n):   # n은 최종 가로길이
    garo_stack = []
    sero_stack = []
    count = 0

    while sum(garo_stack) < n:
        if
            garo_stack.append(20)

                sero_stack.append(20)
                count += 1
            elif garo_stack.append(20):
                sero_stack.append(10)
                count += 1
                sero_stack.append(10)
                garo_stack.append(20)
                count += 1
            elif garo_stack.append(10):
                sero_stack.append(20)
                count += 1
        if sum(garo_stack) == n:
                break
    return count

T = int(input())
for test_case in range(1, T+1):
    width = int(input())
    print(f'{test_case} {paper(width)}')