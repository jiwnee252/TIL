import sys
sys.stdin = open("3499.txt", "r")

T = int(input())  # Test case 개수를 받아오는 코드
for tc in range(1, T + 1):
    N = int(input())  # 카드의 개수 입력
    card_list = input().split()  # 카드들을 리스트로 저장 (알파벳 그대로 사용, 형 변환 없음)

    # 카드를 절반으로 나눌 두 그룹 생성
    first_group = []  # 앞쪽 절반 카드 그룹
    second_group = []  # 뒤쪽 절반 카드 그룹

    # N이 홀수일 경우, 앞쪽 그룹이 한 장 더 많음
    for i in range(N // 2):
        first_group.append(card_list[i])  # 앞쪽 절반 카드 추가
        second_group.append(card_list[(N // 2 + N % 2) + i])  # 뒤쪽 절반 카드 추가 (홀수일 때 가운데 카드 건너뜀)

    # 홀수일 경우, 빠진 가운데 카드(first_group의 마지막 카드)를 따로 추가
    if N % 2 != 0:
        first_group.append(card_list[i + 1])  # 가운데 남은 카드 추가

    # 새로 섞인 카드 리스트 초기화
    new_card_list = [0] * N  # 결과를 저장할 리스트, 크기는 N

    # 카드를 번갈아가며 섞기 (first_group, second_group 교차 삽입)
    for i in range(N // 2):
        new_card_list[i * 2] = first_group[i]  # 짝수 인덱스에 first_group 카드 삽입
        new_card_list[i * 2 + 1] = second_group[i]  # 홀수 인덱스에 second_group 카드 삽입

    # 홀수일 경우 마지막에 남은 카드 추가
    if N % 2 != 0:
        new_card_list[-1] = first_group[-1]  # 마지막에 first_group의 마지막 카드 삽입

    # 최종 결과 출력
    print(f'#{tc}', *new_card_list)
