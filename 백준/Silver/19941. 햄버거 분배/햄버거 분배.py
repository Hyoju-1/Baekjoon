n , k = map(int, input().split()) # n = 식탁 길이 , k = 선택가능거리
table = list(input())

cnt = 0 

for i in range(len(table)):
    if table[i] =="P" : # 식탁에서 있는 사람 먼저 확인
        for j in range(max(0,i-k) , min(n,i+k+1)) : #사람 기준으로 왼쪽, 오른쪽으로 K만큼 확인하기
            if table[j] == "H" : # 햄버거면
                table[j] = "X" # 이미 먹은 햄버거로 바꿈
                cnt += 1    # 먹은 사람 수 1 증가
                break # 다먹었으면 for 문 종료
 
print(cnt)
