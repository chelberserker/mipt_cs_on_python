class Matrix:
    m = None
    n = None
    X = None

    def __init__(self, a, b):
        self.m = a
        self.n = b
        self.X = []
        for i in range(self.m):
            self.X.append([])
            for j in range(self.n):
                self.X[i].append(float(0))

    def get_m(self):
        return self.m

    def get_n(self):
        return self.n

    def get_size(self):
        return self.m, self.n

    def get(self,i,j):
        return self.X[i][j]

    def set(self,i,j,a):
        self.X[i][j] = a

    def __eq__(self, other):
        a = True
        if self.get_m() == other.get_m() and self.get_n() == other.get_n():
            for i in range(self.m):
                for j in range(other.n):
                    if self.X[i][j] != other.X[i][j]:
                        a = False
        else:
            a = False
        return a

    def __add__(self, other):
        result=Matrix(self.get_m(),self.get_n())
        for i in range(self.m):
            for j in range(self.n):
                result.X[i][j] = (float((self.get(i,j))+(other.get(i,j))))
        return result

    def __sub__(self, other):
        result=Matrix(self.get_m(),self.get_n())
        for i in range(self.m):
            for j in range(self.n):
                result.X[i][j] = (self.get(i,j)-other.get(i,j))
        return result

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            result=Matrix(self.m ,self.n)
            for i in range(self.m):
                result.X.append([])
                for j in range(self.n):
                    result.X[i][j] = float(float(self.get(i,j))*float(other))
            return result
        if type(other) == Matrix:
            #FIX ME
            pass


    def __truediv__(self, other):
        result = self * (1/other)
        return result

