# a 난이도 b 기준번호 c 사람수 a는 항상 1
# 1 3 2 : 난이도 1로 3번부터 2명이 기의 상태를 바꾸라
# 명령 M번
# 1 4 3 : 4번부터 상태를 바꾼다 6번이 없으므로 4,5만.

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N명 명령M번
    initial = list(map(int, input().split()))
    order_list = [list(map(int, input().split())) for _ in range(M)]

    # print(N)
    # print(M)
    # print(initial)
    # print(order)

    for order in order_list:
        A = order[1]  # 몇번부터
        B = order[2]  # 몇명이 상태바꿔라

        for i in range(A-1, A+B-1):
            if initial[i] >= N:
                break
            else:
                if initial[i] == 1:
                    initial[i] = 0
                else:
                    initial[i] = 1


    print(initial)


'''
    
3
5 1
1 1 0 0 1
1 3 2
5 3
1 1 0 0 1
1 3 2
1 4 1
1 2 4
5 1
1 1 0 1 0
1 4 1
 
'''