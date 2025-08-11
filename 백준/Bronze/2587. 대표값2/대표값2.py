##아이디어
# 자연수 5개 입력 -> 리스트에 저장
# 평균 : 합을 자연수로 나눈 값
# 중앙값 : 정렬 후 가운데 값 

import sys

input = sys.stdin.readline

nums = [int(input().strip()) for _ in range(5)]  # 5개 숫자 입력

# 평균 계산 (문제에서 자연수 보장)
avg = sum(nums) // 5

# 중앙값 계산
nums.sort()
median = nums[2]  # 정렬 후 가운데 값

print(avg)
print(median)
