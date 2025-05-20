import sys
sys.stdin = open("1288.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s = set()           # 0에서 9까지 본 숫자 목록
    c = 0
    while(len(s) < 10): # 빠진 숫자가 있으면 계속
        c += 1
        num = N * c         #첫 번째에는 N번 양을 세고, 두 번째에는 2N번 양, … , k번째에는 kN번 양을 센다
        nums = str(num)     # 문자열로 변환
        for i in range(len(nums)):
            s.add(nums[i])          # 숫자 종류 확인
    print(f'#{tc} {c*N}')


