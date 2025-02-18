import sys
sys.stdin = open("4871_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    print(V, E) # 노드, 간선        # 특정한 두 개의 노드에 경로가 존재하는가?
    node = [list(map(int, input().split())) for _ in range(E)] 
    print(node)
    start, end = map(int, input().split())
    print(start, end)   # start부터 end까지 경로가 존재하는가.
    # 경로 있으면 1 출력 없으면 0 출력

    visited = [False] * (E + 2)   # E+2인이유? 간선+1 이 노드의개수인데 0번인덱스 고려해서 +1.


    path(node, visited, 1)