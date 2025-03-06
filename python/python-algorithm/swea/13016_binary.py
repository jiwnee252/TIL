import sys
sys.stdin = open("13016_input.txt", "r")


def hex_to_binary(num):
    binary_list = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    binary_num = ''
    for char in num:
        binary_num += binary_list[char]
    return binary_num


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, hx = input().split()
    print(f'#{test_case} {hex_to_binary(hx)}')