import sys; import sys; sys.stdin = open('1221.txt')

num_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
num_dict = { key: val for val, key in enumerate(num_str)}

T = int(input())
tc_num, tmp = input().split()
arr = input().split()

# 카운팅
cnt = [0] * 10
for key in arr:
    val = num_dict[key]
    cnt[val] += 1

lst = []
for i in range(10):
    if cnt[i] != 0:
        lst += [num_str[i]] * cnt[i]

print(' '.join(lst))


