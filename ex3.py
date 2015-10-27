from decimal import Decimal, getcontext
getcontext().prec = 5

S = Decimal(input())
xyear = Decimal(input())/100
xmonth = xyear/12
y = int(input())*12
p = 0
k = (xmonth*(xmonth+1)**y)/((xmonth+1)**y-1)
payment = k*S



"""for i in range(1,y):
    p = p + xmonth**(y-i)
payment = ((S*(xmonth**y))/p)"""
print(payment)
print(payment*y-S)


for i in range(y-1):
    debt = S - payment * i
    print('|', payment, '|', debt, '|', debt*(xmonth), '|', payment-debt*(xmonth))
print('|', debt, '|', 0, '|', debt*(xmonth), '|', debt-debt*(xmonth))
    
