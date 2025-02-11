import sys
sys.stdin = open("1221_input.txt", "r")
# 선택정렬
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = input()
    # print(tc)
    num = list(map(str, input().split()))
    # print(num)
    num2 = []
    for i in range(len(num)) :
        if num[i] == 'ZRO':
            num2.append(0)
        elif num[i] == 'ONE':
            num2.append(1)
        elif num[i] == 'TWO':
            num2.append(2)
        elif num[i] == 'THR':
            num2.append(3)
        elif num[i] == 'FOR':
            num2.append(4)
        elif num[i] == 'FIV':
            num2.append(5)
        elif num[i] == 'SIX':
            num2.append(6)
        elif num[i] == 'SVN':
            num2.append(7)
        elif num[i] == 'EGT':
            num2.append(8)
        else:
            num2.append(9)
    # print(num2)

    for j in range(len(num2)-1):
        min_index = j
        for k in range(j+1, len(num2)):
            if num2[min_index] > num2[k]:
                min_index = k
        num2[j], num2[min_index] = num2[min_index], num2[j]
    # print(num2)

    num3 = []
    for l in range(len(num2)) :
        if num2[l] == 0:
            num3.append('ZRO')
        elif num2[l] == 1:
            num3.append('ONE')
        elif num2[l] == 2:
            num3.append('TWO')
        elif num2[l] == 3:
            num3.append('THR')
        elif num2[l] == 4:
            num3.append('FOR')
        elif num2[l] == 5:
            num3.append('FIV')
        elif num2[l] == 6:
            num3.append('SIX')
        elif num2[l] == 7:
            num3.append('SVN')
        elif num2[l] == 8:
            num3.append('EGT')
        else:
            num3.append('NIN')

    print(f"#{test_case}\n{' '.join(num3)}")