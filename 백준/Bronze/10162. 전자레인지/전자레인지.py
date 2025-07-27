
t = int(input())

a = 300
b = 60
c = 10
a_cnt = b_cnt = c_cnt = 0

if t % c != 0 :
    print(-1)
else:
    a_cnt += t//a 
    t %= a
    
    b_cnt += t//b
    t %= b
    
    c_cnt += t//c
    t %= c
    
    print(a_cnt, b_cnt, c_cnt)
      