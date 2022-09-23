from math import sin
class Equation():
    def __init__(self,function):
        self.function = function
    def __str__(self):
        return '{}(x)'.format(self.function)
    def __call__(self,x):
        return self.function(x)

class PolynomialEquation(Equation):
    def __init__(self,*args):
        self.coefs = list(args)[::-1]
    def __str__(self):
        to_print = ' = 0'
        for i ,coefs in enumerate(self.coefs):
            if coefs  == 0:
                continue
            elif coefs>0:
                to_print =' + {}x^{}'.format(coefs,i)+to_print
            else:
                to_print = ' - {}x^{}'.format(abs(coefs), i) + to_print
        return to_print[2:]
    def __call__(self,x):
        result = 0
        for i ,coefs in enumerate(self.coefs):
            result+=coefs*(x**2)
        return result

class LinearEquation(PolynomialEquation):
    def __init__(self,*args):
        PolynomialEquation.__init__(self,*args)
        self.a = self.coefs[1]
        self.b = self.coefs[0]
    def __str__(self):
        return '{}x +  {}'.format(self.a,self.b)
    def solve(self):
        if self.a == 0:
            if self.b == 0:
                return "Infinite"
            else:
                return set()
        else:
            return -self.b/self.a
class QuadroEquation(PolynomialEquation):
    def __init__(self,*args):
        PolynomialEquation.__init__(self,*args)
        self.a = self.coefs[2]
        self.b = self.coefs[1]
        self.c = self.coefs[0]

    def solve(self):
        d = self.b**2-4*self.a*self.c
        if self.a == 0:
           return LinearEquation(self.coefs[::-1][1]).solve()
        else:
            if d<0:
                return "Нет корней"
            else:
                return {(-self.b+d**0.5)/(2*self.a),(-self.b-d**0.5)/(2*self.a)}
def PolEq(*args):
    if len(args) == 2:
        return LinearEquation.__init__(*args)
    elif len(args) == 3:
        return QuadroEquation.__init__(*args)
    else:
        return PolynomialEquation.__init__(*args)



linear = QuadroEquation(1,10,-3000)
print(linear.solve())