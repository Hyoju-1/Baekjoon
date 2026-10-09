import sys

def main():
    input = sys.stdin.readline
    s = input().strip()
    K, M = map(int, input().split())

    mask = (1 << K) - 1          # K비트만 남기는 틀
    cnt = {}
    v = 0
    for i, ch in enumerate(s):
        v = ((v << 1) | (ch == '1')) & mask   # 새 글자 밀어 넣기
        if i >= K - 1:                         # K글자가 다 찼을 때부터 세기
            c = cnt.get(v, 0) + 1
            if c >= M:
                print(1)
                return
            cnt[v] = c
    print(0)

main()