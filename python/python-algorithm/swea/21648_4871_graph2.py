import sys
sys.stdin = open("21648_4871_input.txt", "r")

def dfs(start, end):
    stack = []  # 빈 스택 생성
    visited = [False] * (V + 1)
    stack.append(start)  # 탐색을 시작할 start 노드를 스택에 넣어준다

    while stack:  # stack이 비어있지 않으면 반복
        now = stack.pop()  # stack에서 pop으로 마지막 추가된 노드를 꺼내서 현재 탐색중인 노드 now로 설정한다
        visited[now] = True  # 현재노드 now를 방문했다면 True로 바꿔주고
        for i in range(1, V + 1):  # 노드 1부터 V까지 반복하면서 now와 연결된 노드들을 탐색하는데
            if not visited[i] and node[now][i]:  # visited[i]==False(만약 방문하지 않은 노드이고) now와 i가 연결된 노드인 경우
                stack.append(i)  # stack에 i를 추가한다 
    if visited[end]:   # visited[end]가  True이면 경로가 있으므로
        return 1  # 1을 반환하고
    else:
        return 0  # 아니면 0을 반환한다.


T = int(input())
for test_case in range(1, T + 1):

    V, E = map(int, input().split())  # V 최대 노드 개수, E 간선 개수
    node = [[0 for i in range(V + 1)] for j in range(V + 1)]   # 노드 i 에서 j 로 가는 길이 있는지를 저장 # 0으로 초기화
    
    for _ in range(E):   # 간선의 개수 E만큼 반복하면서
        start, end = map(int, input().split())  # 각 간선의 출발점, 도착점을 입력받고
        node[start][end] = 1        # start -> end 로 가는 간선이 존재함을 1로 표시

    start, end = map(int, input().split())

    print(f"#{test_case} {dfs(start, end)}")


