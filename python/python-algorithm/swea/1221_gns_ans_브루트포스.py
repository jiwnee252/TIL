import sys

sys.stdin = open('../../../../../Downloads/input.txt')
T = int(input())
for _ in range(T):
    tc, N = input().split()
    words = input().split()
    numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    result = ''

    # numbers 배열에서 첫 번째 ZRO 를 고정해놓고, 주어진 문자열에서
    # ZRO 에 해당하는 친구를 모두 result에 추가한다.
    # 그 다음엔 ONE 고정해놓고,
    # 입력값에서 ONE 에 해당하는 친구를 모두 추가한다.
    for number in numbers:  # 최대 10,000 개
        for word in words:
            if word == number:
                result += word + ' '

    # 시간복잡도 : O(N * 10)
    print(tc)
    print(result)
