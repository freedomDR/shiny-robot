p0 = list(map(float,raw_input().split()))
p1 = list(map(float,raw_input().split()))
p2 = list(map(float,raw_input().split()))

while(1):
    t = float(input())
    p = [p0[v]*(1-t)*(1-t)+p1[v]*2*(1-t)*t+p2[v]*t*t for v in range(2)]
    print p
