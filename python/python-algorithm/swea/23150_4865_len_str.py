import sys
sys.stdin = open("4865.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    
    char_list = []  # str1의 글자가 str2에 몇개 있는지 세서 새 리스트에 담고 해당 리스트에서 최댓값을 출력

    for char in str1:
        char_list.append(str2.count(char))

    print(f'#{test_case} {max(char_list)}')