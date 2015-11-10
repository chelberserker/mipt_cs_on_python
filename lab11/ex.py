class Point:
    def __init__(self, x = 0, y = 0, mass = 0):
        self.x = x
        self.y = y
        self.dist = (x**2+y**2)**0.5
        self.mass = mass
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.mass + other.mass)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, a):
        return Point(self.x*a, self.y*a, self.mass*a)
    def __str__(self):
        return str(self.x) + ' ' + str(self.y)
        
n = int(input())
cm = Point()
dist = Point()       
for i in range(n):
    A = input().split()
    A[0] = int(A[0])
    A[1] = int(A[1])
    a = Point(A[0], A[1], 1)
    if a.dist > dist.dist:
        dist = a
    cm = a + cm 
cm = cm * (1/cm.mass)
print(cm.x, cm.y)
print(dist.x, dist.y, dist.dist)
