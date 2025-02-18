import sys
sys.stdin = open("4871_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    print(V, E)

    # E개의 줄에 걸쳐 출발 도착 노드로 간선 정보가 주어짐