# 공과 잡초 # 1차원 배열 탐색

import sys
sys.stdin = open("14555.txt", "r")

T = int(input())
for tc in range(1, T+1):
    S = input()

    stack = []
    '''
    # 스택에 가능성 있는 것들을 넣어두고 다음 값으로 판단할 수 있음
    ( : stack 추가 (만약에 stack에 무엇인가 들어있다면-> 해당 문자는 절대로 공이될 수 없게 됨) 그래서 stack 모두 pop 후에 '(' push
    | : stack을 확인하고 들어 있는게 만약 '(' 라면 공이 될 수 있음 / 만약에 stack이 비어있다면 그대로 push 
    ) : stack에 뭔가 들어 있으면 pop 하면서 공 + 1
    '''
    count = 0
    for char in S:
        # ( : stack 추가 (만약에 stack에 무엇인가 들어있다면-> 해당 문자는 절대로 공이될 수 없게 됨) 그래서 stack 모두 pop 후에 '(' push
        if char == '(':
            while stack:
                stack.pop()
            stack.append(char)
        # | : stack을 확인하고 들어 있는게 만약 '(' 라면 공이 될 수 있음 / 만약에 stack이 비어있다면 그대로 push
        elif char == '|':
            if stack and stack.pop() == '(':
                count += 1  # 공 개수 증가
            else:
                stack.append(char)
        # ) : stack에 뭔가 들어 있으면 pop 하면서 공 + 1
        elif char == ')':
            if stack and stack.pop():
                count += 1  # 공 개수 증가

    print(f'#{tc} {count}')