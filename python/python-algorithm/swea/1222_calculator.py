import sys
sys.stdin = open("1222.txt", "r")
for test_case in range(1, 11):
    N = int(input())
    tokens = input()
    operator = {'+': 1}
    stack = []
    postfix = []
    # 후위표기법으로 변환
    # 피연산자 만나면 스택에 push
    # 연산자 만나면 필요한 만큼 피연산자를 스택에서 pop하여 연산, 연산결과를 다시 스택에 push
    # 수식이 끝나면 마지막으로 스택을 pop

    for i in range(len(tokens)):
        if tokens[i].isnumeric():  # 숫자이면
            postfix.append(tokens[i])  # 스택에넣고
        elif tokens[i] in operator:  # 연산자이면
            while stack and operator[tokens[i]] <= operator[stack[-1]]:
                # 우선순위가 같거나 작으면
                # tokens[i]우선순위가 더 커질때까지 스택에서 pop
                postfix.append(stack.pop())
            stack.append(tokens[i])
    while stack:
        postfix.append(stack.pop())

    stack2 = []
    for i in range(len(postfix)):
        if postfix[i].isnumeric():
            stack2.append(int(postfix[i]))
        elif postfix[i] in operator:
            stack2.append(stack2.pop() + stack2.pop())

    result = stack2.pop()

    print(f'#{test_case} {result}')