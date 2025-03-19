# 현재 점원을 포함시킬지 말지를 결정해야함
# -> 현재 점원 i, 현재까지의 높이 height_sum를 판단해야함
# 모든 점원을 다 고려했으면 종료해야함 i == N
# 또는 선반 높이에 도달했을때 종료해야함 height_sum >= shelf
# 재귀호출 2가지: 현재 점원 포함하고 남은점원탐색 / 현재 점원 포함하지 않고 남은점원탐색

def dfs(i, height_sum):
    global min_height

    # 현재 높이가 선반 높이보다 큰지 확인
    # 크다면 최소값을 계산한후 종료
    # 선반높이보다 작다면 모든점원을 확인했는지 체크하고 확인했으면 종료
    if height_sum >= shelf:
        diff = height_sum - shelf
        min_height = min(min_height, diff)
        return

    if i == N:
        return

    # 현재 점원 포함
    dfs(i + 1, height_sum + height[i])
    # 현재 점원 미포함
    dfs(i + 1, height_sum)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, shelf = map(int, input().split())    # N 점원의수 B 선반높이
    height = list(map(int, input().split())) # 점원 키 리스트
    S = sum(height) # 점원키의합

    min_height = float("inf")

    # 첫번째 점원 인덱스0 / 초기높이 0
    dfs(0, 0)
    print(f"#{test_case} {min_height}")