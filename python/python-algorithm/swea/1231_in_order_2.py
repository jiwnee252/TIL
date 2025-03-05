import sys
sys.stdin = open("1231_input.txt", "r")

def in_order(i):
    global word
    if i <= N:
        # 왼쪽 자식으로 간다
        in_order(2 * i)
        # 현재노드 처리
        word += tree[i - 1][1]
        # 오른쪽 자식으로 간다
        in_order(2 * i + 1)
    return word

for test_case in range(1, 11):
    N = int(input())   # 정점의 총 수
    tree = [input().split() for _ in range(N)]
    # print(tree)
    word = ''
    print(f'#{test_case} {in_order(1)}')
