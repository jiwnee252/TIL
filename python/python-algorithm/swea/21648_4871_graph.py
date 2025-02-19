import sys
sys.stdin = open("21648_4871_input.txt", "r")

def dfs(start, end, N):   # start # end 목표 노드   # N 전체 노드의 개수
    stack = []  # 빈 스택을 생성한다
    visited = [0] * (N+1)   # 방문여부를 저장, 0부터 N까지이므로 N+1
    while True:
        if visited[start] == 0:     # 만약 현재 노드를 방문한적이 없으면
            visited[start] = 1         # 방문했다고 표시해줌
        for w in adj_list[start]:       # 현재노드 v의 인접노드를 순회하면서
            if visited[w] == 0:     # 만약 인접노드 w를 방문한적이 없으면
                stack.append(start)      # 스택에 현재 노드를 넣고
                start = w               # 인접노드 w를 v로 (더 깊이 탐색ㄱㄱ)
                break               # for break -> while True로
        else:                   # while True 돌다가 인접노드 전부 탐색했는데 모든노드를 방문했을경우
            if stack:           # 스택이 비어있지 않으면
                start = stack.pop()         # 스택에서 꺼내줌 -> 이전노드로 돌아감
            else:               # 스택이 비어있으면
                break           # 탐색종료
    if visited[end] == 1:         # 만약 목표한 노드 g를 방문했다면 1
        return 1
    else:                       # g를 방문하지 못했다면 0
        return 0


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())   # 노드의 최대개수, 간선의 개수
    adj_list = [[] for _ in range(V + 1)]    # 각 노드의 인접리스트를 생성한다   # 0부터 V까지이므로 V+1개 생성

    for _ in range(E):  # E개의 간선을 받아서 인접리스트를 채워줌
        node, edge = map(int, input().split())    # 노드, 간선 정보
        adj_list[node].append(edge)  # 노드에서 간선으로 가는 경로를 adj_list에 저장

    start, end = map(int, input().split())  # 출발노드 start 목표노드 end 입력

    print(f'#{test_case} {dfs(start, end, V)}')