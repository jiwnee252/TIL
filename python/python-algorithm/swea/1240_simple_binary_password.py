import sys
sys.stdin = open("1240_input.txt", "r")

def check_code(pw):
    code = list(pw)  # str이 들어옴..
    odd = []
    even = []
    for i in range(len(code)):
        if i % 2 == 0:   # 홀수자리
            odd.append(code[i])
        else:  # 짝수자리
            even.append(code[i])
    if (sum(odd) * 3 + sum(even)) % 10 == 0:
        return sum(odd) + sum(even)
    else:
        return 0


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    decode = {
        '0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
        '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}

    scanned = []
    # 암호코드는 무조건 1로 끝나니까 # 각 행 순회하면서 뒤에서부터 읽어서  # 1을 찾고 거기서부터 56글자 슬라이싱
    for row in arr:
        for k in range(M-1, -1, -1):
            if row[k] == 1:    # 뒤에서부터 돌아서 1을 발견하면
                scanned.extend(row[k-55:k+1])   # 56글자를 잘라준다.

    # print(scanned)

    digit = []

    # 이제 7글자씩 다시 잘라줄거임
    for p in range(0, 56, 7):
        # 리스트에서 7글자씩 잘랏으니까 하나로합침
        temp = ''.join(map(str, scanned[p:p+7]))
        # 암호 해석한다음에 digit리스트에넣고 digit리스트로 홀짝판단 ㄱㄱ
        digit.append(int(decode[temp]))

    # print(digit)

    print(f'#{test_case} {check_code(digit)}')
