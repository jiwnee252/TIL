# 1289 원재의 메모리 복구하기
import sys
sys.stdin = open('1289.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    memory = input()
    count = 0
    current = '0'
    for bit in memory:
        if bit != current:
            count += 1
            current = bit
    print(f'#{test_case} {count}')



###########################################################
'''
import sys
sys.stdin = open('1289.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    memory = list(map(int, input()))
    now = [0 for _ in range(len(memory))]

    count = 0
    i = 0
    while i <= len(memory)-1:
        if memory[i] != now[i]:
            if memory[i] == 1:
                for j in range(i, len(now)):
                    now[j] = 1
            else:
                for j in range(i, len(now)):
                    now[j] = 0
            count += 1
            i += 1
        else:
            i += 1

    print(f'#{test_case} {count}')
'''