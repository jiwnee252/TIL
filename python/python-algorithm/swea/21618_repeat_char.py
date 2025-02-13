import sys
sys.stdin = open("21618.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    s = input()
    s_list = list(s)
    stack = []
    for char in s_list:
        if not stack:
            stack.append(char)
        else:
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
    # print(stack)

    if len(stack) > 0:
        result = len(stack)
    else:
        result = 0

    print(f'#{test_case} {result}')