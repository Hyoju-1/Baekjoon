t = int(input())

# N번째 손님 (N-1)%H +1 층, (N-1) // H+1호
# 방번호 층*100+호수

for i in range(t):
    h,w,n = map(int, input().split())

    chueng = (n-1)%h+1
    ho = (n-1)//h + 1
    room = chueng*100+ho
    print(room)