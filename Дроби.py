from math import gcd
class Fraction:
    def __init__(self,num,denum = 1):
        self.sign = (num*denum)//(abs(num*denum))
        ob_gcd = gcd(num,denum)
        self.num = abs(num)//ob_gcd
        self.denum = abs(denum)//ob_gcd
    def __str__(self):
        to_print = ""
        if self.sign == -1:
            to_print+='-'
        if self.denum == 1 and self.num>self.denum:
            to_print+='{}'.format(self.num)
        elif self.denum == self.num:
            to_print+='{}'.format(self.num)
        else:
           if  self.num > self.denum:
            to_print += '{} {}'.format(self.num // self.denum, "and")
        to_print += " {}/{}".format(self.num % self.denum, self.denum)
        return to_print
    def __add__(self,second):
        if isinstance(second,int):
            second = Fraction(second)
        new_num = self.sign * self.num * second.denum + second.sign * self.denum * second.num
        new_denum = self.denum * second.denum
        return Fraction(new_num,new_denum)
    def __radd__(self,second):
        return self+second

    def __neg__(self):#создание унарного минуса
        return Fraction(self.sign*self.num*(-1),self.denum)

    def __sub__(self, second):#функция вычитания
        return self + (-second)
    def __rsub__(self,second):
        pass





a = Fraction(5,4)
b = Fraction(4,4)
print(Fraction(121,345)+Fraction(-5,43))
print(Fraction(1,2)+10)