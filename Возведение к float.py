from math import gcd
class Francsion():
    def __init__(self, num, denum = 1):
        self.sign = (num * denum) // (abs(num * denum))
        ob_gcd = gcd(num, denum)
        self.num = abs(num) // ob_gcd
        self.denum = abs(denum) // ob_gcd
    def __float__(self):
        return self.sign*(self.num/self.denum)

print(float(Francsion(1,21)))