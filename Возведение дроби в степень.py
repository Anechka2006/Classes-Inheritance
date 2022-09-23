from math import gcd
class Francsion():
    def __init__(self, num, denum = 1):
        self.sign = (num * denum) // (abs(num * denum))
        ob_gcd = gcd(num, denum)
        self.num = abs(num) // ob_gcd
        self.denum = abs(denum) // ob_gcd
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
    def __pow__(self,second):
        if isinstance(second,int):
            second = Francsion(second)
        new_num = (self.sign*self.num**second.num)
        new_denum = self.denum**second.num
        return Francsion(new_num,new_denum)

    def __int__(self):
        return self.sign*(self.num//self.denum)



print((Francsion(2,3))**3)
a = Francsion(14,8)
int(a)
print(a)


