class Value:
    def __init__(self,data, _children=(), op = ''):
        self.data= data
        self._prev = set(_children)
        self._op = op

    def __repr__(self):
        return f"Value(data = {self.data} )  "

    def __add__(self,other):
        out = Value(self.data + other.data, (self,other), '+')
        return out

    def __mul__(self,other):
        out = Value(self.data * other.data, (self,other), '*')
        return out


a= Value(3)
b= Value(5)
c = a+b
print(c._op)