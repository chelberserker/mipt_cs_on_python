class Matrix:
    m = None
    n = None
    X = None

    def __init__(self, a, b= None):
        if type(a) == int and type(b) == int:
            if a <= 0 or b <= 0:
                raise ValueError
            else:
                self.m = a
                self.n = b
                self.X = []
                for i in range(self.m):
                    self.X.append([])
                    for j in range(self.n):
                        self.X[i].append(float(0))
        elif type(a) == list and b == None:
            self.X = a
            self.m = len(self.X[1])
            self.n = len(self.X)
        else:
            raise ValueError

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
        if self.get_size() != other.get_size():
            raise RuntimeError
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
            if self.get_n() == other.get_m():
                result = Matrix(self.get_m(), other.get_n())
                for i in range(result.get_m()):
                    for j in range(result.get_n()):
                        num = 0
                        for a in range(self.get_m()):
                            for b in range(other.get_n()):
                                num += self.get(a,i) * other.get(b,j)
                        result.X[i][j] = num
            else:
                raise RuntimeError
            return result


    def transpose(self):
        C = Matrix(self.get_n(), self.get_m())
        for i in range(self.get_m()):
            for j in range(self.get_n()):
                C.X[j][i] = self.X[i][j]
        return C


    def __truediv__(self, other):
        result = self * (1/other)
        return result

    def determinant(self):
        if self.get_m() == 2 and self.get_n() == 2:
            return self.get(0, 0)*self.get(1,1)-self.get(0,1)*self.get(1,0)
        elif self.get_m() == 3 and self.get_n() == 3:
            return self.get(0, 0)*self.get(1,1)*self.get(2,2)-self.get(0, 0)*self.get(1,2)*self.get(2,1)-self.get(0, 1)*self.get(1, 0)*self.get(2,2)+self.get(0,1)*self.get(1,2)*self.get(2,0)+self.get(0, 2)*self.get(1,0)*self.get(2,1)-self.get(0, 2)*self.get(1,1)*self.get(2,0)
        else:
            raise RuntimeError


