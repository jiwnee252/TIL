num1 = int(input())
# print(num1)

# 출력: 만들 수 있는 수들의 최대 개수
# 해당 최대 개수의 수들을 차례대로 출력

# 두번째 랜덤한 정수 num2
# 두번째 수는 무조건 첫번째 수보다 작거나 같다.

for num2 in range(1, num1+1):
    numlist = [num1, num2]
    while 1:
        if numlist[-1] >= 0:
            numlist.append(numlist[-2] - numlist[-1])
        else:
            break