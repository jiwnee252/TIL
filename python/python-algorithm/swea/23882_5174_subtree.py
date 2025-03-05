import sys
sys.stdin = open("23882_5174_subtree_input.txt", "r")

def subtree(i):
    global count

    count += 1

    if left[i] != 0:  # 왼쪽 자식이 있으면
        subtree(left[i])
    if right[i] != 0:  # 오른쪽 자식이 있으면
        subtree(right[i])

T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())  # E는 간선의 개수 # 노드는 E+1개
    tree = list(map(int, input().split()))

    left = [0] * (E+2)
    right = [0] * (E+2)
    count = 0

    for i in range(E):
        p, c = tree[i * 2], tree[i * 2 + 1]
        if left[p] == 0:  # 왼쪽 자식이 없다면
            left[p] = c
        else:  # 왼쪽 자식이 있다면 오른쪽 자식에 할당
            right[p] = c

    subtree(N)
    print(f'#{test_case} {count}')
