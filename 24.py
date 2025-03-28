a, b, c = map(int, input().split())

if a > b > c:
    L = [a, b, c]
    print(L[1])
elif b > a > c:
    N = [b, a, c]
elif c > a > b:
    M = [c, a, b]
    print(M[1])
elif a > c > b:
    U = [a, c, b]
elif b > c > a:
    R = [b, c, a]
    print(R[1])
elif c > b > a:
    I = [c, b, a]
    print(I[1])