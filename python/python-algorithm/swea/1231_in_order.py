import sys
sys.stdin = open("1231_input.txt", "r")

def in_order():
    global word
    stack = []
    now = 1  # 루트 노드부터 시작

    while stack or now <= N:
        if now <= N:
            stack.append(now)
            now = 2 * now  # 왼쪽 자식으로 이동
        else:
            now = stack.pop()
            word += tree[now - 1][1]  # 현재 노드 처리
            now = 2 * now + 1  # 오른쪽 자식으로 이동

    return word

for test_case in range(1, 11):
    N = int(input())  # 정점의 총 수
    tree = [input().split() for _ in range(N)]  # 트리 정보 입력

    word = ''
    print(f'#{test_case} {in_order()}')
