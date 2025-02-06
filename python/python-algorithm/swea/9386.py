import sys
sys.stdin = open("9386_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    numlist = input().split('0')
    print(numlist)
    result = len(max(numlist))

    print(f'#{test_case} {result}')