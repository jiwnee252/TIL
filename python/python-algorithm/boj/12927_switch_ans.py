arr = list(input())
    
N = len(arr)
# 전구 상태를 숫자로 변환: Y=1 (켜짐), N=0 (꺼짐)
switches = [1 if ch == 'Y' else 0 for ch in arr]

press_count = 0  # 스위치를 누른 횟수

# 1번 전구부터 N번 전구까지 차례대로 확인
for i in range(1, N+1):
    # 현재 i번 전구가 켜져 있다면, i번 스위치를 누른다.
    if switches[i-1] == 1:
        press_count += 1
        # i번 스위치는 i의 배수 번호를 가진 전구의 상태를 모두 반전시킨다.
        for k in range(i, N+1):
            if k % i == 0:
                switches[k-1] = 1 - switches[k-1]

for switch in switches:
    if switches == 0:
        print("-1")
        break
else:
    print(press_count)

# set으로 중복을 제거하고, 개수가 1개가 아니라면, -1 반환 
# if len(set(switches)) == 1:
#     print(press_count)
# else:
#     print("-1")