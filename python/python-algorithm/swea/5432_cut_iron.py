import sys
sys.stdin = open("5432.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    bar = input()
    # print(bar)

    bar_count = 0

    stack = []
    for i in range(len(bar)):
        if bar[i] == '(':
            stack.append('(')  # 막대기 또는 레이저가 시작햇다는건데. 일단 저장ㄱ
            
        elif bar[i] == ')': # 막대기가 끝낫거나. 레이저가 끝난건데
            # 만약 직전막대기가. ( 이엇으면
            if bar[i-1] == '(':
                # ( ) 은 레이저로 자른거잔음..?
                # 그럼 레이저는빼준다음에
                stack.pop()
                # 스택에남아잇는애들을다잘라준다..
                bar_count += len(stack)
            # 만약 앞에가 )이엇으면
            # ) ) 라는건 막대기가끝낫단거임
            # 모든 막대기는 길이가 다 다르니까 ))일때 여러개가 잘리는 경우는 절대없음 무조건 1개만잘림
            elif bar[i-1] == ')':
                stack.pop()
                bar_count += 1

    print(f'#{test_case} {bar_count}')
