from collections import deque
import sys
input = sys.stdin.readline  # 빠른 입력을 위한 설정 (백준에서 사용하면 좋음)

# 8방향 (상, 하, 좌, 우 + 대각선)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(x, y, graph, visited, w, h):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True  # 현재 위치 방문 처리
    
    # 큐에서 꺼낸 위치 (cx, cy)의 8방향을 확인
    # 땅(1)이고 아직 방문하지 않았으면 방문하고 큐에 추가
    while queue:
        cx, cy = queue.popleft()

        for dir in range(8):  # 8방향 확인
            nx = cx + dx[dir]
            ny = cy + dy[dir]

            # 범위 내 && 땅(1) && 방문하지 않았으면
            if 0 <= nx < w and 0 <= ny < h:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    queue.append((nx, ny))
                    visited[ny][nx] = True

# w,h 를 받고 0,0이면 종료
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break  # 종료 조건
    # 지도를 저장하고, 방문 여부를 기록한 visited 배열 초기화
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    visited = [[False]*w for _ in range(h)]
    count = 0
    # 전체를 돌면서 BFS 수행
    # 아직 방문하지 않은 땅=1 발견하면 BFS 실행
    # BFS가 완료되면 하나의 선 탐색 완료 -> count 증가
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1 and not visited[y][x]:
                bfs(x, y, graph, visited, w, h)
                count += 1  # 새로운 섬 발견

    print(count)
