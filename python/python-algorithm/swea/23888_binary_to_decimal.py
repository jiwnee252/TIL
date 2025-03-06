import sys
sys.stdin = open("23888_input.txt", "r")

# 16진수를 2진수로

def binary_to_decimal(num):
    decimal_num = 0
    pow = 0
    for digit in reversed(num):
        if digit == '1':
            decimal_num += 2 ** pow
        pow += 1
    return decimal_num

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    string = [input().split() for _ in range(N)]
    string2 = ''
    for st in string:
        string2 += st[0]
    result = []
    for i in range(0, len(string2), 7):
        string3 = string2[i:i+7]
        result.append(binary_to_decimal(string3))

    print(f'#{test_case} {" ".join(map(str,result))}')
