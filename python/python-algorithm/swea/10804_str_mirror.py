import sys
sys.stdin = open("10804.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 거꾸로 출력한다..
    tc = input()
    # print(tc)
    result = ""
    for i in range(len(tc)-1, -1, -1):
        if tc[i] == 'q':
            result += 'p'
        elif tc[i] == 'p':
            result += 'q'
        elif tc[i] == 'b':
            result += 'd'
        else:
            result += 'b'

    print(f'#{test_case} {result}')

