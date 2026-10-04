import sys
input = sys.stdin.readline

msg = input().strip()
key = input().strip()

# ── 작업 1: 표 만들기 ──
order = []
seen = set()
for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if ch not in seen:
        order.append(ch)
        seen.add(ch)

table = [order[r*5:(r+1)*5] for r in range(5)]
pos = {}
for k, ch in enumerate(order):
    pos[ch] = (k // 5, k % 5)

# ── 작업 2: 쌍 나누기 ──
pairs = []
i = 0
while i < len(msg):
    a = msg[i]
    if i + 1 < len(msg) and msg[i + 1] != a:
        pairs.append((a, msg[i + 1]))
        i += 2
    elif i + 1 < len(msg):
        filler = 'Q' if a == 'X' else 'X'
        pairs.append((a, filler))
        i += 1
    else:
        pairs.append((a, 'X'))
        i += 1

# ── 작업 3: 암호화 ──
result = []
for a, b in pairs:
    r1, c1 = pos[a]
    r2, c2 = pos[b]
    if r1 == r2:                                  # 같은 행 → 오른쪽 한 칸
        result.append(table[r1][(c1 + 1) % 5])
        result.append(table[r2][(c2 + 1) % 5])
    elif c1 == c2:                                # 같은 열 → 아래 한 칸
        result.append(table[(r1 + 1) % 5][c1])
        result.append(table[(r2 + 1) % 5][c2])
    else:                                         # 다른 행·열 → 열만 교환
        result.append(table[r1][c2])
        result.append(table[r2][c1])

print(''.join(result))