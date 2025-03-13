def run_(lst):
    lst = sorted(lst)
    for i in range(len(lst) - 2):   # range(4)
        if lst[i] + 1 in lst and lst[i] + 2 in lst:
            return True
    return False


def triplet(lst):
    count_ = {}   # 빈 딕셔너리
    for card in lst:    # 카드 하나씩 돌면서
        count_[card] = count_.get(card, 0) + 1     # card가 count에 있으면 해당값을반환 없으면 0반환
        # +1해서 카운트저장
        if count_[card] >= 3:
            return True
    return False

T = int(input())
for test_case in range(1, T + 1):
    cards = list(map(int, input().split()))
    cards_1 = []
    cards_2 = []
    winner = 0
    for i in range(6):
        cards_1.append(cards[2*i])
        if len(cards_1) >= 3:
            if run_(cards_1) or triplet(cards_1):
                winner = 1
                break
        cards_2.append(cards[2*i+1])
        if len(cards_2) >= 3:
            if run_(cards_2) or triplet(cards_2):
                winner = 2
                break
    print(f'#{test_case} {winner}')

