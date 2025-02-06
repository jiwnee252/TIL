import sys
sys.stdin = open("1206_view_input.txt", "r")

# T = int(input())
for test_case in range(1, 11):
    N = int(input())
    # print(N)
    hlist = list(map(int, input().split()))
    # print(hlist)
    # print(len(hlist))

    # 내가 i번째 건물이라하면 i-2, i-1, i+1, i+2 건물의높이가 내높이보다낮으면댐
    # 그럼 i = 2부터시작 ㄱㄱ

    view_count = 0

    i = 2
    for i in range(2, N-2):
        #만약에 내왼쪽2개, 내오른쪽2개 높이의 max값이 내높이-2 한거보다 낮으면 그럴때마다 view_count를 올려줌...
        max_height = max(hlist[i-2], hlist[i-1], hlist[i+1], hlist[i+2])
        if max_height < hlist[i] :
            view_count = view_count + (hlist[i] - max_height) # 내높이 - 주변건물중가장높은높이 (=조망권확보된세대임)

    print(f'#{test_case} {view_count}')
