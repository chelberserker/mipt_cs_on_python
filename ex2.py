def fxn(y,z):
    b = float(0)
    b = 108 - (815-1500 / z) / y
    return b

x0 = float(4)
x1 = float(4.25)
xn=fxn(x1, x0)
xn1 = fxn(xn, x1)

for i in range(30):
    a = fxn(xn1, xn)
    xn=xn1
    xn1=a

print(xn1)
