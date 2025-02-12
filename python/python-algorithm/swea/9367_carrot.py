import sys
sys.stdin = open("9367.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))
    print(N)    # 당근개수
    print(C)    # 당근의크기

    for i in range(N):
        if C[i]+1 == C[i+1]: # 연속으로1개커지ㅏㅁ..
            print()
        else:
            print(1)


    # print(f'#{test_case} {result}')