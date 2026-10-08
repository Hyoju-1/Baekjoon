n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

points = []
for _ in range(m):
    x, y = map(int, input().split())
    points.append((x - 1, y - 1))

# Please write your code here.

# 3. visited(n×n), cnt 준비

visited = [[False]*n for i in range(n)]
cnt = 0

# 4. dfs(r, c, idx):
#      지금 칸이 points[idx]이면 idx +1
#      idx가 ___이면 cnt +1 하고 return
#      4방향 → 범위, 벽, 방문 확인 → 고르고, dfs(nr, nc, idx), 되돌리기
def dfs(r,c,idx):
    global cnt 

    if (r,c) == points[idx] :
        idx = idx +1
    if idx == m:
        cnt += 1 
        return

    
    for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
        nr, nc = dr +r, dc+ c
        if 0 <= nr < n and 0 <= nc < n :
            if grid[nr][nc] == 0 and not  visited[nr][nc] :

                visited[nr][nc] = True
                dfs(nr,nc,idx)
                visited[nr][nc] =  False



sr, sc = points[0]
visited[sr][sc] = True
dfs(sr, sc, 0)

print(cnt)
# 5. 첫 지점(points[0])을 visited 표시하고 dfs 시작
# 6. cnt 출력