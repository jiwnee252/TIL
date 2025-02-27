bingo = [list(map(int, input().split())) for _ in range(5)]
check_list = [list(map(int, input().split())) for _ in range(5)]
checklist = []

for check in check_list:
    for c in check:
        checklist.append(c)
        # extend로

print(checklist)  # 사회자가 부른 숫자.

# 숫자를 하나 지울 때마다 빙고인지 체크 해야함.

# 한개 지웠으면 checked += 1
# 한줄 채웠으면 count += 1

def check_if_bingo(bingo):
    count = 0
    # 가로 체크
    if :
        count += 1
    # 세로 체크
    if :
        count += 1
    # 대각선 체크
    if (bingo[k][4-k] == 0 for k in range(5)):
        count += 1
    if (bingo[k][k] == 0 for k in range(5)):
        count += 1

    return count


# 사회자가 부른 숫자를 순회한다
for k in checklist:
    # 빙고판을 순회한다
    for i in range(5):
        for j in range(5):
            # 만약 checklist의 숫자가 빙고에 잇으면
            # 해당칸을 0으로 체크해준다.
            if bingo[i][j] == k:
                bingo[i][j] = 0
    if k >= 12:

# 빙고 3줄 이려면 최소 12개부름
# 사회자가 11개 부를때까진 체크 안하고.
# 12개부터는 한개 지울때마다 빙고 체크 하면됨 함수호출해서.


# 방금 지운 숫자가 (i, j)라면
# 가로
# di = [0, 0, 0, 0, 0]
# dj = [-2, 1, 0, 1, 2]

# 세로
# di = [-2, -1, 0, 1, 2]
# dj = [0, 0, 0, 0, 0]

# 대각선 좌하 우상
# di = [-2, -1, 0, 1, 2]
# dj = [-2, -1, 0, 1, 2]

# 대각선 좌상 우하
# di = [-2, -1, 0, 1, 2]
# dj = [2, 1, 0, -1, -2]

