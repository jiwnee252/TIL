T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = list(input().strip())
    print(arr)

    bin_arr = []

    for i in arr:
        temp = f'{int(i, 16):04b}'  # 이진수 변환
        bin_arr.append(temp)
        if arr[0] == 1:
            # bin_arr.insert(0)
            # bin_arr.insert(0)

    bin_str = ''.join(map(str, bin_arr))
    print(bin_str)

    pw_dict = {
        '001101': '0', '010011': '1', '111011': '2', '110001': '3', '100011': '4',
        '110111': '5', '001011': '6', '111101': '7', '011001': '8', '101111': '9'
    }

    pw = []

    for k in range(2, len(bin_str), 6):
        while len(bin_str) - k >= 6:
            temp = bin_str[k:k+6]
            pw.append(pw_dict[str(temp)])
            break
        # if len(bin_str) - k < 6:
        #     temp2 = bin_str[k:]
        #     pw.append(temp2)

    print(f'#{test_case} {" ".join(pw)}')