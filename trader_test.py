from random import randint, choice
from time import time


class OperationType(object):

    _time = 0.0

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
        tt = time() - OperationType._time
        OperationType._time = tt
        return tt

    def helper(self):
        pass


class Plus(OperationType):

    MAX = 999999

    def __init__(self):
        OperationType.__init__(self, "Plus")

    def get_one(self):
        a = randint(0, Plus.MAX) / 1000
        b = randint(0, Plus.MAX) / 1000

        self.timer()
        return str(a) + " + " + str(b), a + b


class Minus(OperationType):

    MAX = 999999

    def __init__(self):
        OperationType.__init__(self, "Minus")

    def get_one(self):
        a = randint(0, Minus.MAX) / 1000
        b = randint(0, Minus.MAX) / 1000

        self.timer()
        return str(a) + " - " + str(b), a - b


class Multiply(OperationType):

    MAX = 999

    def __init__(self):
        OperationType.__init__(self, "Multiply")
        self._a = 0
        self._b = 0

    def get_one(self):
        a = randint(0, Multiply.MAX)
        b = randint(0, Multiply.MAX)

        while a > 99 and b > 99:
            a = randint(0, Multiply.MAX)
            b = randint(0, Multiply.MAX)

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
        a = randint(0, Square.MAX)

        self.timer()
        return str(a) + "^2 ", a**2


class Generator(object):

    def __init__(self):
        self._type_lst = [Plus(), Minus(), Divide(), Square(), Multiply(), Multiply(), Multiply(), Multiply()]

    def get_one(self):
        problem = choice(self._type_lst)
        prob, answer = problem.get_one()
        print(prob)
        right = True
        while True:
            tt = input()

            if tt == "p":
                right = False
                break

            if tt == "h":
                problem.helper()
                right = False

            try:
                if abs(float(tt) - answer) < 1e-5:
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
        for i in range(N):
            self.get_one()

        for it in self._type_lst:
            print(it.get_summary())


if __name__ == "__main__":
    generator = Generator()
    generator.start(20)
