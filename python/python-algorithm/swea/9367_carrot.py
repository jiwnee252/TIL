import sys
sys.stdin = open("9367.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())    # 당근개수
    C = list(map(int, input().split())) # 당근의크기

    count = 1
    count_list = []

    for i in range(N-1):    
        if C[i] < C[i+1]:   # 다음당근보다 작으면
            count += 1
            count_list.append(count)
        else:   # 다음당근이 크거나작으면
            count = 1
            count_list.append(count)

    # print(max(count_list))

    print(f'#{test_case} {max(count_list)}')