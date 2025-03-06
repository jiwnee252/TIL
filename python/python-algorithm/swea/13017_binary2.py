T = int(input())

def decimal_to_binary(n):
    binary_num = ''
    i = 0
    while n > 0:
        if n < (2 ** -i):
            binary_num += '0'
        else:
            n = n - (2 ** -i)
            binary_num += '1'
        i += 1
    if len(binary_num[1:]) <= 12:
        return binary_num[1:]
    else:
        return 'overflow'

for test_case in range(1, T + 1):
    N = float(input())
    print(f'#{test_case} {decimal_to_binary(N)}')