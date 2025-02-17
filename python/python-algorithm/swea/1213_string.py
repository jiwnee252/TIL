import sys
sys.stdin = open("1213.txt", "r", encoding='UTF8')

for test_case in range(1, 11):
    N = int(input())
    find = input()
    word = input()
    count = 0
    for i in range(len(word)):
        if word[i] == find[0]:
            if word[i:i+len(find)] == find:
                count += 1
    print(f'#{test_case} {count}')