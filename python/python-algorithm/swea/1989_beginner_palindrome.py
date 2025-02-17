import sys
sys.stdin = open("1989.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N = input()
    result = 1

    for i in range(len(N)):
        if N[i] != N[len(N)-i-1]:
            result =0
        
    print(f'#{test_case} {result}')