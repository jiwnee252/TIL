import sys
sys.stdin = open("1219.txt", "r")

def dfs(start, end):  # 출발점, 도착점, 인접리스트
    stack = []  # 빈 스택 생성
    visited = [0] * 100  # 방문여부 저장

    while True:
        if visited[start] == 0:     # 방문안했음
            visited[start] = 1         # 방문처리해준다
        for a in adj_list[start]:      # 인접리스트의 노드를 돌면서 확인해줄건데
            if visited[a] == 0:     # 인접한노드 방문안햇으면
                stack.append(start)         # 스택에 방금 있던 노드를 저장 해준담에
                start = a               # a로 이동을 해준다.
                break                   # break해주고 다시    if visited[start] == 0:   여기로돌아가서 반복ㄱㄱ
        else:   # 만약 start를 방문 했었으면
            if stack:   # 스택을 확인해주는데 스택에 노드가잇으면 뒤돌아갈수 ㅇ
                start = stack.pop()     # 맨뒤에있는걸 꺼내서 거기로 뒤돌아감
            else:   # 스택이 비어잇으면 다돈거임
                break
    if visited[end] == 1:
        return 1
    else:
        return 0

##################################################################################

for tc in range(1, 11):

    tc, edge = map(int, input().split()) # 테케 번호, 간선의 개수
    graph = list(map(int, input().split())) # 순서쌍 입력받음
    adj_list = [[] for _ in range(100)]   # 인접리스트를 만들어주는데
    for i in range(edge):
        v, w = graph[i*2], graph[i*2 +1]
        adj_list[v].append(w)       # 단방향
        # adj_list[w].append(v)   # 이거하면양방향임

    print(f'#{tc} {dfs(0, 99)}')
