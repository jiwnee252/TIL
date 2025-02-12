import sys

sys.stdin = open('../../../../../Downloads/input.txt')
T = int(input())
for _ in range(T):
    tc, N = input().split()
    words = input().split()
    result = []
    number_words = []

    # 문자 -> 숫자로 바꾸기 위한 dict
    str_to_number = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    number_to_str = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}
    # 문자를 숫자로 바꾸는 과정
    for word in words:
        number_words.append(str_to_number[word])

    # 숫자로 바뀐 리스트를 정렬
    number_words.sort()

    # 숫자를 문자로 바꾸는 과정
    for number_word in number_words:
        result.append(number_to_str[number_word])

    print(tc)
    print(" ".join(result))
