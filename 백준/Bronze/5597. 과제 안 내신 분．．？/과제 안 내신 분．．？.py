# 전체 학생 번호
all = set(range(1,31))

# 제출
did = set(int(input()) for i in range(28))
          
#미제출
no = sorted(all - did)

print(no[0])
print(no[1])