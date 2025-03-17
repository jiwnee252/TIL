from itertools import product

def calc_(nums, operators):
    result = nums[0]
    for j in range(1, len(nums)):
        if operators[j-1] == '+':
            result += nums[j]
        elif operators[j-1] == '-':
            result -= nums[j]
    return result

def solution(numbers, target):
    numbers.insert(0, 0)  # 앞에 0을 넣어줘서 연산이되도록 한다.. 0을 안넣고 할수는 없을까 생각 해보기.
    global k
    count = 0
    for i in product(k, repeat=len(numbers)-1):
        op_list = i
        result = calc_(numbers, op_list)
        if result == target:
            count += 1
    return count

k = ['+', '-']


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))

'''
다른 사람의 풀이

def dfs(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
print(dfs([1, 1, 1, 1, 1], 3))
print(dfs([4, 1, 2, 1], 4))

'''
'''

def dfs(index, current_sum, numbers, target):
    # 모든 숫자를 다 사용했을 때
    if index == len(numbers):
        # current_sum이 target과 같다면 1을 반환 (이 경우가 하나의 방법)
        return 1 if current_sum == target else 0
    
    # 현재 숫자에 대해 두 가지 선택: 더하기 또는 빼기
    add_case = dfs(index + 1, current_sum + numbers[index], numbers, target)
    subtract_case = dfs(index + 1, current_sum - numbers[index], numbers, target)
    
    # 두 경우의 결과를 합산하여 반환
    return add_case + subtract_case

def solution(numbers, target):
    return dfs(0, 0, numbers, target)

# 예시 실행
print(solution([1, 1, 1, 1, 1], 3))  # 출력: 5
print(solution([4, 1, 2, 1], 4))     # 출력: 2



'''