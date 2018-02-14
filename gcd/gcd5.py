def gcd(a, b):
    if m<n:
        (m,n) = (n,m)
    if (m%n) == 0:
        return n
    else:
        diff=m-n
        return(gcd(max(n,diff), min(n,diff)))

def p(s):
    print(s)

if __name__ == "__main__":
    p("input a:")
    a = int(input())
    p("input b:")
    b = int(input())
    p("gcd of "+str(a)+" and "+str(b)+" is:")
    print(gcd(a, b))
