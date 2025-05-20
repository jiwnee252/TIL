import sys
sys.stdin = open("14555.txt", "r")

T = int(input())
for tc in range(1, T+1):
    S = input()
    stack = []
    count = 0
    for char in S:
        if char == '(':
            while stack:
                stack.pop()
            stack.append(char)
        elif char == '|':
            if stack and stack.pop() == '(':
                count += 1
            else:
                stack.append(char)
        elif char == ')':
            if stack and stack.pop():
                count += 1
    print(f'{tc} {count}')

'''
T = int(input())
for tc in range(1, T+1):
    S = input()
    full_ball = S.count('()')
    open_only = S.count('(')
    close_only = S.count(')')
    count = full_ball + (open_only - full_ball) + (close_only - full_ball)

    print(f'#{tc} {count}')
'''
