def amb(a,b):
    c=0
    v=0
    for i in range(1,a):
    
        if a % i ==0:
            c=c+i
           # print(c)
            
    for j in range(1,b):
        if b %j==0:
            v=v+j
     
            
    if b == c:
        if a == v:
            print(f"{a} and {b} are the amicable number")
    else:
        print("not amb")
amb(220,284)
