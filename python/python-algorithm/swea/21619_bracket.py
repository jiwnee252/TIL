import sys
sys.stdin = open("21619.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    b_list = input()
    # print(b_list)
    stack = []
    result = 1  # 일단 참이라고 가정
    for i in range(len(b_list)):
        if b_list[i] == '(':
            stack.append(b_list[i])   # 그러면 스택에 추가
        elif b_list[i] == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
            else:
                result = -1
    if stack:
        result = -1

    print(f'#{test_case} {result}')