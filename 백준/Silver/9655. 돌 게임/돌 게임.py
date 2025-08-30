#n = 1 → SK이 돌 1개 가져감 → SK 승리
#n = 2 → SK이 1개만 가져갈 수 있음 → 돌 1개 남음 → CY이 가져감 → CY 승리
#n = 3 → SK이 3개 가져가면 끝 → SK 승리
#n = 4 → SK이 1개 가져가면 CY이 3개 가져가고 끝,SK이 3개 가져가면 CY이 1개 가져가고 끝 → 결국 CY 승리
#n = 5 → SK이 1개 가져가면 CY은 4개 상황(=CY 패 상태) → SK 승리
#패턴을 보면 짝수일 때 CY 승, 홀수일 때 SK 승 

n = int(input())

if n % 2 == 0:
    print("CY")
else:
    print("SK")
