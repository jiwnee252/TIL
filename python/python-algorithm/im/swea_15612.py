# 15612 체스판 위의 룩 배치
import sys
sys.stdin = open('15612.txt', 'r')

def r(chesspan):
    rook = 'O'
    rook_count = 0
    for i in range(8):
        for j in range(8):
            if chesspan[i][j] == 'O':
                rook_count += 1
                if rook_count != 8:
                    return 'no'
                else:
                    # 모든 행에서도 겹치면 안되고 모든 열에서도 겹치면 안됨
                    pass
            return 'yes'


T= int(input())
for test_case in range(1, T+1):
    chesspan = [list(map(str, input())) for _ in range(8)]

    print(f'#{test_case} {r(chesspan)}')