#이중 반복문으로 풀기에는 O(NxM)이라 최악의 경우 시간 초과 위험이 있음

# 정렬 후 이진 탐색으로 B배열을 정렬해 두고, A의 각 원소 a에 대해서 B에서 a보다 작은 원소의 개수를 빠르게 찾으면 됨
# bisect모듈을 쓰면 B안에서 a보다 작은 원소의 개수를 바로 구할 수 있음
# 전체 쌍의 개수는 각 a에 대해 구한 개수를 모두 합한 값임

import sys
import bisect

input = sys.stdin.readline

T = int(input().strip())  # 테스트 케이스 개수

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    B.sort()  # B 정렬 (이진 탐색 준비)

    count = 0
    for a in A:
        # bisect_left: B에서 a보다 작은 값의 개수 반환
        count += bisect.bisect_left(B, a)

    print(count)
