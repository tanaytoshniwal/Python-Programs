def gcd(a, b):
    if m<n:
        (m,n) = (n,m)
    while (m%n)!=0:
        diff=m-n
        (m,n)=(max(n,diff),min(n,diff))
    return(n)

def p(s):
    print(s)

if __name__ == "__main__":
    p("input a:")
    a = int(input())
    p("input b:")
    b = int(input())
    p("gcd of "+str(a)+" and "+str(b)+" is:")
    print(gcd(a, b))
