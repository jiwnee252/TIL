import sys
sys.stdin = open("1289.txt", "r")

T = int(input())
for tc in range(1, T+1):
    original_memory = input()

    count = 0
    is_one = False
    for bit in original_memory:
        if is_one and bit == '0':
            count += 1
            is_one = False
        elif not is_one and bit == '1':
            count += 1
            is_one = True

    print(f'#{tc} {count}')


