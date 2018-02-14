def gcd(a, b):
    for i in range(1, min(a, b)+1):
        if (a%i) == 0 and (b%i) == 0:
            mrcf = i
    return (mrcf)

def p(s):
    print(s)

if __name__ == "__main__":
    p("input a:")
    a = int(input())
    p("input b:")
    b = int(input())
    p("gcd of "+str(a)+" and "+str(b)+" is:")
    print(gcd(a, b))
