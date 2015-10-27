import sys 

a = float(1)
e = 0.5
while (a + e) != a:
    laste = e
    e = e/1.00001
print(laste)
print(1.0+laste)
print(sys.float_info.epsilon)
print(1.0+sys.float_info.epsilon/2)
