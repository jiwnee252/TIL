bingo = [list(map(int, input().split())) for _ in range(5)]
check_list = [list(map(int, input().split())) for _ in range(5)]
checklist = [] # 사회자가 부른 숫자.

for check in check_list:
        checklist.extend(check)

def check_if_bingo(bingo):
    count = 0  # 한줄 채웠으면 올리기
    # 가로 체크
    for row in range(5):
        if sum(bingo[row]) == 0:
            count += 1
    # 세로 체크
    for k in range(5):
        if all(bingo[l][k] == 0 for l in range(5)):
            count += 1
    # 대각선 체크
    if all(bingo[k][4-k] == 0 for k in range(5)):
        count += 1
    if all(bingo[k][k] == 0 for k in range(5)):
        count += 1
    return count

# 사회자가 숫자 부를때마다 횟수체크
speak = 0
# 사회자가 부른 숫자를 순회한다
for k in checklist:
    # 사회자가 숫자를 불럿으므로 횟수1체크
    speak += 1
    # 빙고판을 순회한다
    for i in range(5):
        for j in range(5):
            # 만약 checklist의 숫자가 빙고에 잇으면
            # 해당칸을 0으로 체크해준다.
            if bingo[i][j] == k:
                bingo[i][j] = 0
    if speak >= 12:
        b_count = check_if_bingo(bingo)
        if b_count >= 3:
            # print(k)
            print(speak)
            break

# 빙고 3줄 이려면 최소 12개부름
# 사회자가 11개 부를때까진 체크 안하고.
# 12개부터는 한개 지울때마다 빙고 체크 하면됨 함수호출해서.
