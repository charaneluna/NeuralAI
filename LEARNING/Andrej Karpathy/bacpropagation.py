

#  This will be an example of manual backpropagation through a perceptron of two layers 

# first lets call our class of Value 

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

    
def back():
    h = 0.001
    a =Value(2.0, label = 'a')
    b= Value (-3.0, label = 'b')
    c = Value (10.0, label = 'c')
    e = a*c, e.label = 'e'
    d = e+c, d.label = 'd'
    f = Value (-2.0, label = 'f')
    L = d+f, L.label = 'L'
    l1 = L.data

    a =Value(2.0, label = 'a')
    b= Value (-3.0, label = 'b')
    c = Value (10.0, label = 'c')
    e = a*c, e.label = 'e'
    d = e+c, d.label = 'd'
    f = Value (-2.0, label = 'f')
    L = d+f, L.label = 'L'
    l2 = L.data 






    pass