def gcd(a, b):
    i = min(a, b)
    while i>0:
        if (a%i) == 0 and (b%i) == 0:
            return i
        else:
            i = i-1
    return (common_factors[-1])

def p(s):
    print(s)

if __name__ == "__main__":
    p("input a:")
    a = int(input())
    p("input b:")
    b = int(input())
    p("gcd of "+str(a)+" and "+str(b)+" is:")
    print(gcd(a, b))
