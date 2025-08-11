##아이디어 : 
# B는 재배열 불가
# S를 최소화하려면 A의 큰 값은 B의 작은 값에 곱하고, A의 작은 값은 B의 큰 값에 곱하도록 A를 재배열해야 함
# 따라서 A를 오름차순 정렬, B를 내림차순 정렬한 후, 같은 인덱스끼리 곱해 더하면 S의 최소값이 됨.

import sys

input = sys.stdin.readline

# 1) N 입력
n = int(input().strip())

# 2) 배열 A와 B 입력
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 3) A는 오름차순, B는 내림차순 정렬
A.sort()
B_sorted = sorted(B, reverse=True)

# 4) 최소 S 계산
S = sum(a * b for a, b in zip(A, B_sorted))


print(S)
