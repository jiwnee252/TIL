import sys
sys.stdin = open("1289.txt", "r")

T = int(input())
for tc in range(1, T+1):
    original_memory = input()

    # 초기값 0에서 원래 메모리로 돌아가는 횟수
    # 0에서 1로 만드는 것을 1번
    # 1에서 0으로 만드는 것도 횟수 1번
    # 원래 메모리에서 변경되는 부분의 횟수를 세면 총 바꿔야 하는 횟수가 나오게 됨
    # 0 에서 1을 만날 때! count += 1
    # 1 에서 0을 만날 때! count += 1
    count = 0   # 총 변경 횟수를 세기위한 count
    is_one = False  # is_one flag 변수는 False 라면 이전 값이 0이고, True 라면 이전 값이 1이었음을 의미
    # is_one 은 이전 데이터의 정보를 가지고 있는 flag 변수
    # flag 변수는 뭔가요?
    # flag 변수는 주로 상태를 저장하여 사용하기 위한 변수
        # 만약 문이 열리면 오른손을 들고
        # 만약 문이 닫혀있다면 왼손을 드세요!
        # 여기에서 문의 상태 를 저장하는 것이 바로 flag 변수
    for bit in original_memory:
        if is_one and bit == '0':   # 1에서 0으로 변경되는 것을 확인 flag를 이용해서 확인
            count += 1
            is_one = False      # 0으로 변경되었기 때문에 flag 변수를 False로 갱신
        elif not is_one and bit == '1': # 0에서 1로 변경되는 부분
            count += 1
            is_one = True

    print(f'#{tc} {count}')
