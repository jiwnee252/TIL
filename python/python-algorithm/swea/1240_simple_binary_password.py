import sys
sys.stdin = open("1240_input.txt", "r")

def check_code(pw):
    code = list(pw)  # str이 들어옴..
    odd = []
    even = []
    for i in range(len(code)):
        if int(i) % 2 == 0:   # 홀수자리
            odd.append(int(code[i]))
        else:  # 짝수자리
            even.append(int(code[i]))
    if (sum(odd) * 3 + sum(even)) % 10 == 0:
        return sum(odd) + sum(even)
    else:
        return 0

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    dict = {
        '0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
        '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}

    # 암호코드 이외의 부분은 0
    # 주어진 arr에서 암호코드가 어딘지 찾아야됨
    # 암호코드는 무조건 1로 끝나니까 # 각 행 순회하면서 뒤에서부터 읽어서  # 1을 찾고 거기서부터 56글자 슬라이싱

    password = []

    for row in arr:
        for item in range(len(row)):
            if row[item] == 1:
                password.extend(row[item-55:item+1])

    password_split = []
    for p in range(0, len(password), 7):      # 7글자씩 잘라야됨
        temp = ''.join(map(str, password[p:p+7]))
        password_split.append(temp)

    # print(password_split)

    decoded = ''
    for item in password_split:
        digit = dict.get(item)
        decoded += str(digit)

    print(decoded)

    print(f'#{test_case} {check_code(decoded)}')
