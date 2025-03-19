di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(now_x, now_y, num_):
    
    # 7자리가 되면 더이상 탐색ㄴㄴ
    if len(num_) == 7:
        num_list.add(num_)
        return

    for d in range(4):
        # 4방향 새로운좌표
        new_x = now_x + di[d]
        new_y = now_y + dj[d]
        # 새로운 좌표가 격자판 안에 있다면
        if 0 <= new_x < 4 and 0 <= new_y < 4:
            # 현재 숫자에 새로운 숫자를 붙인다.
            dfs(new_x, new_y, num_ + arr[new_x][new_y])

T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(str, input().split())) for _ in range(4)]

    num_list = set()   # 중복숫자 거르기위해서...

    # 격자판의 모든칸(i, j)에서 탐색을 시작한다.
    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])

    print(f"#{test_case} {len(num_list)}")
