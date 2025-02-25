import sys
sys.stdin = open("21675_4874_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 숫자를 만나면 스택에 append
    # 연산자를 만나면 스택에서 두개를 pop한뒤 스택에 append
    # .는 스택에서 숫자를 꺼내 출력
    tokens = input().split()
    # operator = ["+", "-", "/", "*"]
    stack = []

    for token in tokens:
        try:
            if token.isdigit():
                stack.append(int(token))
            elif token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                if b == 0:  # 0으로 나눴을때 오류
                    print(f'#{test_case} error')
                    break
                else:
                    stack.append(b // a)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == '.':
                if len(stack) == 1:
                    print(f'#{test_case} {stack.pop()}')
                else:
                    print(f'#{test_case} error')
        except:
            print(f'#{test_case} error')
            break