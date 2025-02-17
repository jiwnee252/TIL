import sys
sys.stdin = open("1215.txt", "r")

# T = int(input())
for test_case in range(1, 11):
    length = int(input())    # 찾아야 하는 회문의 길이
    arr = [list(map(str, input())) for _ in range(8)]   # 가로
    arr2 = list(map(list, zip(*arr)))   # 세로

    # 길이가 length인 회문의 개수를구하라
    # 가로 개수 + 세로 개수
    count = 0
    for row in arr:
        for i in range(8-length+1):
            if row[i:i+length] == row[i:i+length][::-1]:
                count += 1

    for row in arr2:
        for i in range(8-length+1):
            if row[i:i + length] ==  row[i:i+length][::-1]:
                count += 1

    print(f'#{test_case} {count}')


