def solution(numbers, hand):    # numbers: 번호배열 # hand: 왼손잡이, 오른손잡이
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]

    # 손가락 쓸때마다 어떤 손가락인지 스택에 넣어준다
    hand_stack = []
    left = [[3,0]] # 초기좌표
    right = [[3,2]]

    # 주어진 numbers를 하나씩 순회하면서
    for k in numbers:
        if k in [1, 4, 7]:
            hand_stack.append('L')
            if k == 1:
                left.append([0, 0])
            elif k == 4:
                left.append([1, 0])
            elif k == 7:
                left.append([2, 0])
        elif k in [3, 6, 9]:
            hand_stack.append('R')
            if k == 3:
                right.append([0, 2])
            elif k == 6:
                right.append([1, 2])
            elif k == 9:
                right.append([2, 2])
        elif k in [2, 5, 8, 0]:  # keypad[0][1] keypad[1][1] keypad[2][1] keypad[3][1]
            # 현재 왼손의좌표는 keypad[left[-1][0]][left[-1][1]] 오른손좌표는 keypad[right[-1][0]][right[-1][1]]

            for p in range(4):
                p = [2, 5, 8, 0].index(k)
                left_distance = abs(left[-1][0] - p) + abs(left[-1][1] - 1)
                right_distance = abs(right[-1][0] - p) + abs(right[-1][1] - 1)
                if left_distance != right_distance:
                    if left_distance > right_distance:
                        hand_stack.append('R')
                        right.append([p, 1])
                    elif left_distance < right_distance:
                        hand_stack.append('L')
                        left.append([p, 1])
                elif left_distance == right_distance:
                    if hand == 'left':
                        hand_stack.append('L')
                        left.append([p, 1])
                    elif hand == 'right':
                        hand_stack.append('R')
                        right.append([p, 1])
                break

    answer = ''.join(hand_stack)
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))