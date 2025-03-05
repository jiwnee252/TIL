import sys
sys.stdin = open("23883_5176_input.txt", "r")

def bs(i):
    global num
    if i <= N:
        # 왼쪽 자식으로 간다
        bs(2 * i)
        # 현재노드에 num할당
        tree[i] = num
        num += 1
        # 오른쪽 자식으로 간다
        bs(2 * i + 1)
    return num

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1) # 노드 저장할 배열
    num = 1
    bs(1)   # 루트 노드부터 순회
    print(f'#{test_case} {tree[1]} {tree[N//2]}')
