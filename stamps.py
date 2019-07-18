def stamps(x):
    a,b,c=0,0,0
    t,s=0,0
    
    while x>(5*t+2*s+c):
        c=c+1
    
        while x>(5*t+2*b):
            b=b+1
            c=0
            if x==5*t+2*b:
                s=b
            else:
                s=b-1
            
            while x>(5*a):
                a=a+1
                b=0
                if x==5*a:
                    t=a
                else:
                    t=a-1
 
    return (t,s,c)                                                   

print (stamps(5))
print (stamps(4))
print (stamps(3))
print (stamps(2))
print (stamps(1))

