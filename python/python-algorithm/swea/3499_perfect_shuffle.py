import sys
sys.stdin = open("3499.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # 카드개수
    deck = list(map(str, input().split()))
    # print(N)
    # print(deck)
    for i in range(N):
        if N % 2 == 0:  # 카드가 짝수개
            deck1 = deck[:N//2]
            deck2 = deck[N//2:]
            shuffle = []
            for j in range(N//2):
                shuffle.append(deck1[j])
                shuffle.append(deck2[j])
        else:   # 카드가 홀수개
            deck1 = deck[:(N+1)//2]
            deck2 = deck[(N+1)//2:]
            shuffle = []
            for j in range((N+1)//2 - 1):
                shuffle.append(deck1[j])
                shuffle.append(deck2[j])
            shuffle.append(deck1[-1])
    print(f'#{test_case} {" ".join(shuffle)}')