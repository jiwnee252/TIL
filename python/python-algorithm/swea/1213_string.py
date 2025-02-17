import sys
sys.stdin = open("1213.txt", "r", encoding='UTF8')

T = int(input())
for test_case in range(1, T + 1):
    find = input()
    word = input()
    print(find)
    print(word)