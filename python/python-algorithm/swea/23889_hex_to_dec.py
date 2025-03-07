def hex_to_dec(array):
    bin_arr = []
    for a in array:
        temp = f'{int(a, 16):04b}'   # 이진수 변환
        bin_arr.append(temp)

    # print(bin_arr)

    bin_str = ''.join(bin_arr)

    # print(bin_str)

    result = []

    # 앞에서부터 7비트씩 묶
    for i in range(0, len(bin_str), 7):
        temp = bin_str[i:i+7]
        # 십진수로변환
        dec_temp = int(temp, 2)
        result.append(dec_temp)
    # print(result)

    return ' '.join(map(str, result))

T = int(input())
for test_case in range(1, T + 1):
    arr = input()
    arr2 = list(arr)
    # print(arr2)

    print(f'#{test_case} {hex_to_dec(arr2)}')
