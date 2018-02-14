def gcd(a, b):
    factors_a = []
    for i in range(1, a+1):
        if (a%i) == 0:
            factors_a.append(i)

    factors_b = []
    for i in range(1, b+1):
        if (b%i) == 0:
            factors_b.append(i)

    common_factors = []
    for i in factors_a:
        if i in factors_b:
            common_factors.append(i)
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
