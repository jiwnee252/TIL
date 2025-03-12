T = int(input())   # 팀 수
for test_case in range(1, T+1):
    N, M = map(int, input().split())    # N 팀원의수 # M 명령의횟수 # a 난이도 # b 기준번호 # c 비교범위
    # a는 항상 2
    start = list(map(int, input().split()))
    order_list = [list(map(int, input().split())) for _ in range(M)]

    for order in order_list:
        A = order[0]  # 난이도
        B = order[1]  # 기준번호
        C = order[2]  # 비교 범위

        for i in range(1, C+1):
            # 인덱스는 0 사람은 1번부터 시작하니까 -1 해준다
            # 인덱스 범위설정
            if 0 <= B - 1 - i < N and 0 <= B - 1 + i < N:
                # 양쪽을 비교했는데 다를경우 넘어감
                if start[B - 1 - i] != start[B - 1 + i]:
                    continue
                # 양쪽을 비교했는데 같을경우
                elif start[B - 1 - i] == start[B - 1 + i]:
                    if start[B - 1 - i] == 0 and start[B - 1 + i] == 0:
                        start[B - 1 - i] = 1
                        start[B - 1 + i] = 1
                    elif start[B - 1 - i] == 1 and start[B - 1 + i] == 1:
                        start[B - 1 - i] = 0
                        start[B - 1 + i] = 0
            else:
                break

    print(f'#{test_case} {" ".join(map(str,start))}')
