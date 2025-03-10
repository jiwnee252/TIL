import sys
sys.stdin = open("20349_input.txt", "r")

def shuffle(card, N):
    split = N - (37 * N) // 100
    # overhand shuffle
    card_37 = card[split:]
    card_63 = card[:split]
    card_37.extend(card_63)
    card_overhand_shuffled = card_37
    # perfect shuffle
    if N % 2 == 0:
        card_first_half = card_overhand_shuffled[:N // 2]
        card_second_half = card_overhand_shuffled[N // 2:]
    else:
        card_first_half = card_overhand_shuffled[:N//2 + 1]
        card_second_half = card_overhand_shuffled[N//2 + 1:]
    card_perfect_shuffled = []
    j = 0
    while j < N//2 + 1:
        if j >= len(card_first_half):
            break
        card_perfect_shuffled.append(card_first_half[j])
        if j >= len(card_second_half):
            break
        card_perfect_shuffled.append(card_second_half[j])
        j += 1
    return card_perfect_shuffled

t = int(input())
for test_case in range(1, t + 1):
    N, T = map(int, input().split())
    card = [i for i in range(1, N+1)]
    k = 0
    while k < T:
        card = shuffle(card, N)
        k += 1

    print(f'#{test_case} {" ".join(map(str, card))}')
