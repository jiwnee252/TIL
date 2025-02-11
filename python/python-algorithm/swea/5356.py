import sys
sys.stdin = open("5356.txt", "r")

# zip? 자릿수안맞으면안대서.안될거가틈..

T = int(input())
for test_case in range(1, T + 1):
    tc = [list(input().split()) for _ in range(5)]

    tc2 = []
    for item in tc:
        tc2.append(list(item[0]))
    # print(tc2)

    for i in range(5):   # 각 테스트 케이스는 5줄
        for j in range(len(tc2[i])):   # 테케의 각 요소의 길이
            # tc2[1][0]이 [0][1]로 가고
            # tc2[2][1] 이 [1][2]로
            if j <= i:
                tc2[i][j], tc2[j][i] = tc2[j][i], tc2[i][j]
            else:
                tc2.append(0)
    print(tc2)
    # print(f'#{test_case} {result}')