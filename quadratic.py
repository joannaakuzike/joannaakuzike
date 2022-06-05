from cmath import sqrt


def solve_quadratic(a,b,c):
    import cmath
    a =float(input("a:  "))
    b =float(input("b:  "))
    c =float(input("c:  "))
    if a == 0: 
        raise ValueError("The coefficient 'a' cannot be zero")
    if a > 0 and c > 0 : return "none"

    d = (b**2)-(4*a*c)

    sol1 = (-b-cmath.sqrt(d))/(2*a) 
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    
    return (sol1,sol2)