import math

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

    def tanh(self): # since this is inside of the class we cant do tanh(h) but instead we do n.tanh
        x = self.data
        t = (math.exp(2*x)-1)/(math.exp(2*x)+1)
        return Value(t,(self,), 'tanh')

#brief example of a simplified manual backpropagation 

# def back():

#     h = 0.001
#     a =Value(2.0, label = 'a')
#     b= Value (-3.0, label = 'b')
#     c = Value (10.0, label = 'c')
#     e = a*c, e.label = 'e'
#     d = e+c, d.label = 'd'
#     f = Value (-2.0, label = 'f')
#     L = d+f, L.label = 'L'
#     l1 = L.data

#     a =Value(2.0, label = 'a')
#     b= Value (-3.0, label = 'b')
#     c = Value (10.0, label = 'c')
#     e = a*c, e.label = 'e'
#     d = e+c, d.label = 'd'
#     f = Value (-2.0, label = 'f')
#     L = d+f, L.label = 'L'
#     l2 = L.data 

# end of manual backpropagation example 


def back2():
    #inputs
    x1= Value(2.0,label = 'x1')
    x2= Value(0.0,label = 'x2')
    #weights
    w1=Value(-3.0,label='w1')
    w2=Value(1.0,label='w2')
    #bias
    b= Value(6.7,label='b')
    # x1*w1 and x2*w2

    x1w1 = x1*w1 ; label= 'x1w1'
    x2w2= x2*w2; label = 'x2w2'

    x1w1x2w2= x1w1+x2w2 ; label = 'x1w1x2w2'

    n= x1w1x2w2 + b
    o = n.tanh() # this introduces a non linear function to the system so that it can have more complex thinking and not just a linear thinking
    







    pass