def pack_carrots(carrots, N):

    diff = 9999  # 개수 차이
    min_diff = 9999
    best_pack = None

    for i in range(1, N):
        for j in range(i + 1, N):

            # 일단 세개의 상자로 나눠준다...
            s = carrots[:i]
            m = carrots[i:j]
            l = carrots[j:]

            # # 같은 크기의 당근은 같은 상자에 들어있어야 한다.
            # for k in s:
            #     if k in m or k in l:
            #         continue
            # for k in m:
            #     if k in s or k in l:
            #         continue
            # for k in l:
            #     if k in s or k in m:
            #         continue

            # 한 상자에 N//2개를 초과하는 당근이 있어서도 안된다.
            if len(s) > N // 2 or len(m) > N // 2 or len(l) > N // 2:
                continue

            # 각 상자에 든 당근의 개수
            size = [len(s), len(m), len(l)]
            # 각 상자에 든 당근의 개수 차이
            diff = max(size) - min(size)
            # min_diff = 9999
            # 각 상자에 든 당근의 개수 차이가 최소가 되어야함.
            if diff < min_diff:
                min_diff = diff
                best_pack = [s, m, l]

    if not best_pack:
        return -1
    else:
        return min_diff


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()

    print(f'#{test_case} {pack_carrots(carrots, N)}')








'''
N개의 당근을 주문하면 대, 중, 소 상자로 구분해 포장해야 한다. 같은 크기의 당근은 같은 상자에 들어있어야 한다. 비어있는 상자가 있으면 안 된다. 한 상자에 N / 2 개(N이 홀수면 소수점버림)를 초과하는 당근이 있어서도 안 된다. 앞의 조건을 만족하면서도, 각 상자에 든 당근의 개수 차이가 최소가 되도록 포장해야 한다.그리고 이때의 개수 차이를 서류에 표시한다. 새로운 주문이 들어와 N개의 당근을 밭에서 뽑아왔다.대, 중, 소 상자를 각각 저울에 올려 포장해보는 대신, 뽑은 당근의 크기를 입력하면 모든 조건을 확인하는 프로그램을 만들어 쉽게 당근을 포장할 수 있게 도와보자. 

예시1)

뽑아온 당근이 3개이고, 크기가 1 2 3 이라면 다음과 같이 포장할 수 있다.
소[1], 중[2], 대[3], 상자에 든 당근의 개수 차이는 0

예시2)

당근이 5개이고 크기가 1 1 1 2 3 이라면, 조건(1)~(3) 을 만족하는 포장은 다음과 같다.
소[1 1 1], 중[2], 대[3], 당근의 개수 차이는 2

하지만 이 경우 5 / 2개(2개)를 초과하는 상자가 있으므로 조건(4)를 만족하지 못한다.

예시3)

당근이 8개이고, 크기가 1 2 3 4 5 6 7 8 인 경우이다.우선 다음과 같이 포장할 수도 있다.
소[1 2 3 4], 중[5], 대[6 7 8], 당근의 개수 차이는 3

하지만 다음과 같이 포장해야 조건(5)를 만족한다.

소[1 2 3], 중[4 5 6], 대[7 8], 당근의 개수 차이는 1

또는 다음과 같은 경우도 조건(5)를 만족한다.

소[1 2], 중[3 4 5], 대[6 7 8], 당근의 개수 차이는 1

'''

    # 포장할수 없는경우 -1 포장할수 있는경우 상자에 들어있는 당근개수 차이가 최소일때의 차이값 출력