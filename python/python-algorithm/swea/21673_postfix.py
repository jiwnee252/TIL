import sys
sys.stdin open="21673.txt", "r"

T = int(input())
for test_case in range(1, 4):
    # 피연산자 만나면 스택에 push
    # 연산자 만나면 필요한 만큼 피연산자를 스택에서 pop하여 연산, 연산결과를 다시 스택에 push
    # 수식이 끝나면 마지막으로 스택을 pop

    tokens = input()

    operator = {'+':1, '*':2, '/':2}
    stack = []
    result = []

    for i in range(len(tokens)):
        if tokens[i].isnumeric():   # 숫자이면
            result.append(tokens[i])     # 스택에넣고
        elif tokens[i] in operator: # 연산자이면
            while stack and operator[tokens[i]] <= operator[stack[-1]]:
            # 우선순위가 같거나 작으면
            # tokens[i]우선순위가 더 커질때까지 스택에서 pop
                result.append(stack.pop())
            stack.append(tokens[i])
    while stack:
        result.append(stack.pop())

    # print("".join(result))
    print(f'#{test_case} {"".join(result)}')