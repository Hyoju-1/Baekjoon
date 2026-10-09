import sys
input = sys.stdin.readline

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 칸을 낮은 순서대로 정렬 (높이, 행, 열)
cells = sorted((grid[r][c], r, c) for r in range(N) for c in range(N))

def possible(D):
    dp = [[1] * N for _ in range(N)]        # 자기 혼자면 길이 1
    for h, r, c in cells:                   # 낮은 칸부터
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                nh = grid[nr][nc]
                if nh < h and h - nh <= D:  # 더 낮은 이웃에서, 차이 D 이하로 올라올 수 있으면
                    dp[r][c] = max(dp[r][c], dp[nr][nc] + 1)
        if dp[r][c] >= K:
            return True
    return False

lo, hi = 1, 10**8
if not possible(hi):            # 차이를 무제한 허용해도 안 되면
    print(-1)
else:
    ans = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if possible(mid):
            ans = mid
            hi = mid - 1        # 최솟값 찾기
        else:
            lo = mid + 1
    print(ans)