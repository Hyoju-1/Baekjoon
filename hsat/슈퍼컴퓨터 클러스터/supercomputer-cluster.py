import sys
input = sys.stdin.readline

n, b = map(int, input().split())
comp = list(map(int, input().split()))

def possible(X):                  # 최저 성능을 X로 만들 수 있나?
    cost = 0
    for a in comp:
        if a < X:
            cost += (X - a) ** 2
            if cost > b:
                return False
    return True

lo, hi = min(comp), min(comp) + 10**9
ans = lo
while lo <= hi:
    mid = (lo + hi) // 2          # mid = 시험해 볼 최저 성능
    if possible(mid):
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)