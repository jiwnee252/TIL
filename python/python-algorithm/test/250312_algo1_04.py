def one(stone, i, j):   # 그냥 뒤집는다
    for k in range(i-1, i+j-1):
        if k >= N:
            break
        else:
            if stone[k] == 1:
                stone[k] = 0
            elif stone[k] == 0:
                stone[k] = 1
    return stone


def two(stone, i, j):   # i번째부터 j개의 돌을 i번째 돌의 색으로 바꾼다
    for k in range(i-1, i+j-1):
        if k >= N:
            break
        else:
            if stone[i-1] == 1:
                stone[k] = 1
            elif stone[i-1] == 0:
                stone[k] = 0
    return stone


def three(stone, i, j):
    # i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해 각각 같은색이면 뒤집고 다른색이면 그대로둔다
    for k in range(N):
        if 0 <= i-j < N and 0 <= i+j < N:
            if stone[i-j] == stone[i+j]:  # 같은색이면
                if stone[i-j] == 1:
                    stone[i-j] = 0
                    stone[i+j] = 0
                elif stone[i-j] == 0:
                    stone[i - j] = 1
                    stone[i + j] = 1
    return stone

def k(stone, w):
    if w == 1:
        stone = (one(stone, i, j))
    elif w == 2:
        stone = (two(stone, i, j))
    elif w == 3:
        stone = (three(stone, i, j))
    return stone


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())   # N 돌의개수 # M 뒤집기횟수
    stone = list(map(int, input().split()))   # 돌의 초기상태
    arr = [list(map(int, input().split())) for _ in range(M)]
    # i 기준위치 j 작업할 돌의 개수 w 수행할 작업 방식
    for item in arr:
        i = item[0]  # 기준위치
        j = item[1]  # 작업할 돌의 개수
        w = item[2]  # 수행할 작업 방식
        # print(w)
        # print(item)
        for item_ in item:
            if w == 1:
                stone = (one(stone, i, j))
            elif w == 2:
                stone = (two(stone, i, j))
            elif w == 3:
                stone = (three(stone, i, j))

    # tc3. 1번작업후 계속 반복 하려면 ??
    print(f'#{test_case} {" ".join(map(str, stone))}')
