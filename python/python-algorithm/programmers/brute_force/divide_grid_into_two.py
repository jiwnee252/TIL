def bfs(n, wires):

    return

def solution(n, wires):
    # bfs??

    graph = [[] for _ in range(n+1)]
    answer = -1
    return answer

    # 완전탐색..
# i번에서 나가는 간선을 큐에 저장
# 하나씩 bfs 탐색

# n 송전탑의 개수 # wires 전선정보
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))

'''
def build_tree(edges):
    wires = {}
    for parent, child in edges:
        if parent not in wires:
            wires[parent] = []
        wires[parent].append(child)
        
        # 자식 노드가 트리에 없다면 자식 노드도 트리에 추가 (빈 리스트로)
        if child not in wires:
            wires[child] = []
    
    return wires

# 예시 리스트
edges = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

# 트리 생성
tree = build_tree(edges)

# 결과 출력
print(tree)


'''

'''
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
queue = [(0, 0)]

while queue:
    i, j = queue.pop(0)
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < M:
            if maze[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                queue.append([ni, nj])
print(visited[N-1][M-1] + 1)
'''