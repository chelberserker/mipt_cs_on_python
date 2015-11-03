def setchanging(X, Y, Z, K):
    E = set()
    T = X.difference(Y)
    U = Z.difference(K)
    I = K.difference(X)
    F = Y.difference(Z)
    L = T.intersection(U)
    M = I.intersection(F)
    E = L.union(M)
    return E



A = set('0123456789')
B = set('02468')
C = set('12345')
D = set('56789')

print(setchanging(A, B, C, D))
