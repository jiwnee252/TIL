import sys
sys.stdin = open("1244_input.txt", "r")

def recur(numbers, exchange, count=0):
    if count == exchange:
        return numbers

    numbers_ = numbers[count:]   # 교환을 n번 했다면, [n:] 슬라이싱한 범위를검사.

    if not numbers_:            # 슬라이싱했는데 빈배열이면 더이상못하니깐 리턴
        return numbers

    max_num = max(numbers_)      # numbers에서 가장 큰 수를 찾아준다.
    max_index = -1               # numbers에서 가장 큰 수의 인덱스를 구해줄건데
    for i, num in enumerate(numbers_):
        if num == max_num:
            # 만약 큰수가 중복이면 더뒤에있는수를 선택.
            max_index = i

    numbers_[0], numbers_[max_index] = numbers_[max_index], numbers_[0]   # 제일 앞에 있는수와 제일 큰수를 교환한다.
    numbers[count:] = numbers_  # numbers_를 업데이트한다
    count += 1

    return recur(numbers, exchange, count)

T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    numbers = list(map(int, str(arr[0])))
    exchange = arr[1]
    count = 0
    print(f'#{test_case} {"".join(map(str, recur(numbers, exchange)))}')


# 다시풀어야됨 이거 틀렸음