import sys
sys.stdin = open("1234.txt", "r")

for test_case in range(1, 11):
    tc, num = input().split()
    # print(num)

    password = list(num)
    print(password)
    stack = []
    for i in password:
        # 스택에 아무것도 없으면 현재값을 추가
        if len(stack) == 0:
            stack.append(i)
        # 스택에 머가잇으면..
        else:
            # 스택의 맨마지막숫자가 현재숫자와 다를경우
            if stack[-1] != i:
                stack.append(i)
            # 스택의 맨마지막숫자가 현재숫자와 같을경우
            else:
                stack.pop()
    print(f'#{test_case} {"".join(stack)}')