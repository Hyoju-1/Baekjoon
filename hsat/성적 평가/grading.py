import sys
input = sys.stdin.readline

n = int(input())
scores = [list(map(int, input().split())) for i in range(3)]


def get_rank(scores):
    desc = sorted(scores, reverse = True) #내림차순 정렬

    rank = {}
    for idx,s in enumerate(desc):
        if s not in rank:
            rank[s] = idx +1  #인덱스는 0부터라 +1
    
    return [rank[s] for s in scores] #원래 순서대로 등수 리스트

totals = [a+b+c for a,b,c in zip(scores[0], scores[1],scores[2])]
    
for s in [scores[0],scores[1],scores[2],totals]:
    print(*get_rank(s))