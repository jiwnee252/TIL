import sys
sys.stdin = open("5356.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = [list(map(str, input().split())) for _ in range(5)]
    print(tc)

    result = [[0] * 15 for _ in range(15)]


    for i in range(5):
        for j in range(len(tc[i])):


    print(result)
    '''
    
    print(tc)

    # print(f'#{test_case} {result}')
    '''