class Drob:
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def __str__(self):
        return f'{self.m}/{self.n}'

    def __add__(self, other):
        m1 = self.m * other.n + other.m * self.n
        n1 = self.n * other.n
        return Drob(m1, n1)

    def __sub__(self, other):
        m1 = self.m * other.n - other.m * self.n
        n1 = self.n * other.n
        return Drob(m1, n1)

    def __mul__(self, other):
        m1 = self.m * other.m
        n1 = self.n * other.n
        return Drob(m1, n1)

    def __truediv__(self, other):
        m1 = self.m * other.n
        n1 = self.n * other.m
        return Drob(m1, n1)

d1 = Drob(1, 3)
d2 = Drob(2, 5)
print(f'{d1} + {d2} = {d1 + d2}')

d3 = Drob(1, 3)
d4 = Drob(1, 4)
print(f'{d3} - {d4} = {d3 - d4}')

d5 = Drob(1, 6)
d6 = Drob(1, 8)
print(f'{d5} * {d6} = {d5 * d6}')

d7 = Drob(1, 3)
d8 = Drob(3, 1)
print(f'{d7} / {d8} = {d7 / d8}')
