# k가 소수이면 0, 합성수이면 k를 포함하는 연속한 소수 p와 q를 찾음. 길이는 q-p
# 문제에서 최대 범위가 주어진 경우 Limit을 정해서 미리 소수를 구해두는게 나음.

import sys

input = sys.stdin.readline

LIMIT = 1299709  # 문제에서 주어진 최대 범위

# ------------------------------
# 1. 에라토스테네스의 체
# ------------------------------
is_prime = [True] * (LIMIT + 1)
is_prime[0] = is_prime[1] = False

i = 2
while i * i <= LIMIT:
    if is_prime[i]:
        j = i * i
        while j <= LIMIT:
            is_prime[j] = False
            j += i
    i += 1

# 소수 리스트 만들기
primes = []
for i in range(2, LIMIT + 1):
    if is_prime[i]:
        primes.append(i)

# ------------------------------
# 2. 입력 처리 & 출력
# ------------------------------
T = int(input().strip())
for _ in range(T):
    k = int(input().strip())

    if is_prime[k]:
        print(0)
    else:
        # --- bisect 대신 직접 이진 탐색 ---
        low, high = 0, len(primes) - 1
        while low <= high:
            mid = (low + high) // 2
            if primes[mid] <= k:
                low = mid + 1
            else:
                high = mid - 1
        
        # 이제 low가 k보다 큰 첫 소수의 위치
        q = primes[low]
        p = primes[low - 1]
        print(q - p)
