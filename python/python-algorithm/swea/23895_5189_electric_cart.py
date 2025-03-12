import itertools
import sys
sys.stdin = open("23895_5189_input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    num = [i for i in range(1, N+1)]
    # print(num)

    route_list = list(itertools.permutations(num[1:]))
    # print(route_list)

    # 원래 리스트
    new_route_list = [(1,) + item + (1,) for item in route_list]

    # print(new_route_list)

    list_ = []
    for item in new_route_list:
        list__ = []
        for j in range(len(item) - 1):
            k = (item[j], item[j+1])
            list__.append(k)
        list_.append(list__)
    print(list_)

    battery_list = []
    for item in list_:
        battery = 0
        for item_ in item:
            battery += arr[item_[0]][item_[1]]

        battery_list.append(battery)
    print(battery_list)


    print(f'#{test_case} {}')