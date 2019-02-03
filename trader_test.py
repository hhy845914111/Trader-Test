from random import randint, choice
from time import time
from math import sqrt


class OperationType(object):

    time_save = 0.0

    def __init__(self, typename):
        self.right_count = 0
        self.wrong_count = 0
        self.typename = typename

    def get_one(self):
        pass

    def right(self):
        self.right_count += 1

    def wrong(self):
        self.wrong_count += 1

    def get_summary(self):
        return f"{self.typename}: correct: {self.right_count}, wrong: {self.wrong_count}\n"

    @staticmethod
    def timer():
        tt = time()
        dt = tt - OperationType.time_save
        OperationType.time_save = tt
        return dt

    def helper(self):
        pass


class Plus(OperationType):

    MAX = 99999

    def __init__(self):
        OperationType.__init__(self, "Plus")

    def get_one(self):
        a = randint(0, self.MAX) / 100
        b = randint(0, self.MAX) / 100

        self.timer()
        return str(a) + " + " + str(b)


class FracMultiply(OperationType):

    MAX = 20

    def __init__(self):
        OperationType.__init__(self, "FracMultiply")

    def get_one(self):
        a = randint(0, self.MAX)
        b = randint(0, self.MAX)
        c = randint(0, self.MAX)
        d = randint(0, self.MAX)

        while not c:
            c = randint(0, self.MAX)

        while not d:
            d = randint(0, self.MAX)

        return str(a) + " / " + str(b) + " * " + str(c) + " / " + str(d), a / b * (c / d)


class FracDivide(OperationType):

    MAX = 20

    def __init__(self):
        OperationType.__init__(self, "FracDivide")

    def get_one(self):
        a = randint(0, self.MAX)
        b = randint(0, self.MAX)
        c = randint(0, self.MAX)
        d = randint(0, self.MAX)

        while not c:
            c = randint(0, self.MAX)

        while not d:
            d = randint(0, self.MAX)

        while not b:
            b = randint(0, self.MAX)

        return str(a) + " / " + str(b) + " / (" + str(c) + " / " + str(d) + ")", a / b / (c / d)


class Minus(OperationType):

    MAX = 99999

    def __init__(self):
        OperationType.__init__(self, "Minus")

    def get_one(self):
        a = randint(0, Minus.MAX) / 100
        b = randint(0, Minus.MAX) / 100

        self.timer()
        return str(a) + " - " + str(b), a - b


class Multiply1(OperationType):

    MAX = 999

    def __init__(self):
        OperationType.__init__(self, "Multiply")
        self._a = 0
        self._b = 0

    def get_one(self):
        a = randint(0, self.MAX)
        b = randint(0, self.MAX)

        while a > 99 and b > 99:
            a = randint(0, self.MAX)
            b = randint(0, self.MAX)

        self._a = a
        self._b = b

        self.timer()
        return str(a) + " * " + str(b), a * b

    def helper(self):
        if self._a <= 99:
            print(self._a // 10 * self._b * 10, self._b * (self._a % 10))
        else:
            print(self._b // 10 * self._a * 10, self._a * (self._b % 10))


class Multiply2(OperationType):

    MAX = 99

    def __init__(self):
        OperationType.__init__(self, "Multiply")
        self._a = 0
        self._b = 0

    def get_one(self):
        a = randint(0, self.MAX)
        b = randint(0, self.MAX)

        while a > 99 and b > 99:
            a = randint(0, self.MAX)
            b = randint(0, self.MAX)

        self._a = a
        self._b = b

        self.timer()
        return str(a) + " * " + str(b), a * b

    def helper(self):
        if self._a <= 99:
            print(self._a // 10 * self._b * 10, self._b * (self._a % 10))
        else:
            print(self._b // 10 * self._a * 10, self._a * (self._b % 10))


class Divide(OperationType):

    MAX = 99

    def __init__(self):
        OperationType.__init__(self, "Divide")

    def get_one(self):
        a = randint(0, Divide.MAX)
        b = randint(0, Divide.MAX)

        self.timer()
        return str(a * b) + " / " + str(b), a


class Square(OperationType):

    MAX = 99

    def __init__(self):
        OperationType.__init__(self, "Square")

    def get_one(self):
        a = randint(0, self.MAX)

        self.timer()
        return str(a) + "^2", a**2


class SquareRoot(OperationType):
    
    MAX = 999

    def __init__(self):
        OperationType.__init__(self, "Squre Root")

    def get_one(self):
        a = randint(0, self.MAX)

        self.timer
        return "sqrt " + str(a), sqrt(a)


class Generator(object):

    def __init__(self):
        self._type_lst = [Plus(), Minus(), Divide(), Square(), Multiply2(), FracDivide(), FracMultiply(), SquareRoot(), SquareRoot(), SquareRoot(), SquareRoot()]

    def get_one(self):
        problem = choice(self._type_lst)
        prob, answer = problem.get_one()
        print(prob)

        right = True
        while True:
            tt = input()

            if tt == "p":
                right = False
                print(answer)
                break

            if tt == "h":
                problem.helper()
                right = False

            try:
                if abs(eval(tt) - answer) < 1e-5:
                    print(str(problem.timer()) + "s")
                    break
            except ValueError:
                pass
            right = False

        if right:
            problem.right()
        else:
            problem.wrong()

    def start(self, N):
        OperationType.time_save = time()
        for i in range(N):
            self.get_one()
            print("\n")

        for it in self._type_lst:
            print(it.get_summary())


if __name__ == "__main__":
    generator = Generator()
    generator.start(20)
