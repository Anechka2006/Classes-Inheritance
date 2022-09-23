class IntError(Exception):
    def __str__(self):
        return "С отрицательными числами ничего не выйдет"
class InstError(IntError):
    def __str__(self):
        return "Нужно вводить только числа"
class AmountError(IntError):
    def __str__(self):
        return "Жаль но из этого треугольник не сделаешь"
class TriagleChecker():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        if not isinstance(self.a,int) \
                or not isinstance(self.b,int) \
                or not isinstance(self.c,int) :
            raise InstError
        elif self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise IntError
        elif self.a+self.c<=self.b \
                or self.a+self.b<=self.c \
                or self.b+self.c<=self.a:
            raise AmountError


try:
    tr = TriagleChecker('a',6,4).is_triangle()
    print("Ура из этого можно построить треугольник!")
except IntError as err:
    print(err)
except AmountError as err:
    print(err)
except InstError as err:
    print(err)