import sys
sys.stdin = open("21617_4866.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    code = input()
    # print(code)
    stack = []
    result = 1    # 1이라고가정
    for i in range(len(code)):
        if code[i] == '{' or code[i] == '}':
            if code[i] == '{':
                stack.append(code[i])
            elif code[i] == '}':
                if stack:
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        result = 0
                else: result = 0
        elif code[i] == '(' or code[i] == ')':
            if code[i] == '(':
                stack.append(code[i])
            elif code[i] == ')':
                if stack:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        result = 0
                else: result = 0
    if stack:
        result = 0

    print(f'#{test_case} {result}')