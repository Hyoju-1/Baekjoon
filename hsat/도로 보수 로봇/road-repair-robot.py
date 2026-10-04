import sys
input = sys.stdin.readline

n, k = map(int, input().split())
holes = sorted(map(int, input().split()))

def possible(L):                  # 길이 L 패치로 K개 이하로 덮을 수 있나?
    count = 0
    i = 0
    while i < n:
        start = holes[i]
        count += 1
        while i < n and holes[i] <= start + L - 1:
            i += 1
    return count <= k

lo, hi = 1, holes[-1] - holes[0] + 1     # 탐색 대상 = 패치 길이
ans = hi
while lo <= hi:
    mid = (lo + hi) // 2                 # mid = 시험해 볼 패치 길이
    if possible(mid):
        ans = mid
        hi = mid - 1                     # 더 짧은 길이도 되는지 확인
    else:
        lo = mid + 1
print(ans)