def dfs(v, N):  # v출발, N마지막 정점
    visited = [0] * (N + 1)  # 방문표시
    stack = []  # 스택
    path = []
    while True:
        if visited[v] == 0:  # 첫 방문이면
            visited[v] = 1
            path.append(v)
        for w in adj_list[v]:  # v에 인접하고 방문안한 w가 있으면
            if visited[w] == 0:
                stack.append(v)  # 현재 정점 push
                v = w  # w로 이동
                break  # for w 를 break
        else:  # 더 이상 갈 곳이 없는 경우
            if stack:  # pop
                v = stack.pop()
            else:  # 스택이 비어있으면
                break  # while True를 break
    return path

V, E = map(int, input().split())  # V 정점의 개수 # E 간선의 개수
graph = list(map(int, input().split()))
adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    v, w = graph[i * 2], graph[i * 2 + 1]
    adj_list[v].append(w)
    adj_list[w].append(v)
print('#1', '-'.join(map(str, dfs(1, V))))