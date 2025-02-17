# https://www.acmicpc.net/problem/2798

N, M = map(int, input().split())
# print(N)    # 주어진 카드의 개수
# print(M)    # 카드의 최대합
cards = list(map(int, input().split()))
# print(cards)

# card_sum <= M
# N장의 카드 중 3장의 카드를 골랐을 때, 3장의 합 <= M 이면서 최대한 크게

sum_list = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if cards[i] + cards[j] + cards[k] <= M:
                sum_list.append(cards[i] + cards[j] + cards[k])
print(max(sum_list))

    # 3장의 합 M 부터 거꾸로...

    # print(result)