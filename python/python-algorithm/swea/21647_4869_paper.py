import sys
sys.stdin = open('21647_4869.txt', 'r')

def paper(x):
    if x == 1:
        return 1
    elif x == 2:
        return 3
    else:
        return paper(x-2)*2 + paper(x-1)

# print(paper(3))

T = int(input())
for test_case in range(1, T+1):
    width = int(input())
    print(f'#{test_case} {paper(width//10)}')

