import sys
sys.stdin = open("5356.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    words = [list(input().split()) for _ in range(5)]
    # words2 = [list(item[0]) for item in words]
