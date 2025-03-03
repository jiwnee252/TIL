from collections import deque
import sys

sys.stdin = open("21773_5099_pizza_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # 화덕 크기 / 피자 개수
    cheese = list(map(int, input().split()))  # 처음 치즈 양

    # 피자 번호와 치즈 양을 튜플 형태로 저장
    fire = deque([[i + 1, cheese[i]] for i in range(M)])
    in_fire = deque(list(fire)[:N])  # 화덕 안의 피자
    out_fire = deque(list(fire)[N:])  # 남은 피자
    # print(in_fire)
    # print(out_fire)
    while len(in_fire) > 1:  # 화덕에 피자가 1개남으면 멈춤
        pizza_num, cheese_amount = in_fire.popleft()
        cheese_amount //= 2  # 치즈 반으로
        if cheese_amount > 0:
            in_fire.append([pizza_num, cheese_amount])  # 도로넣음
        elif out_fire:
            in_fire.append(out_fire.popleft())  # 남은피자넣음

    print(f'#{test_case} {in_fire[0][0]}')