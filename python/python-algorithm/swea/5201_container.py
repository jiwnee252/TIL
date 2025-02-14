import sys
sys.stdin = open('5201.txt', 'r')
T = int(input())
for test_case in (1, T+1):
    N, M = input().split()
    print(N, M) # N : 컨테이너 개수   # M : 트럭 개수
    W, T = [list(map(int, input().split())) for _ in range(2)]
    print(W, T) # W : N개의 화물의 무게 리스트   # T : M개 트럭의 적재용량

    truck_list = []
    container_list = []
    container_weight = 0

    for truck in T.sort():
        if



    # print(f'#{test_case} {result}')