class Foo():
    def __init__(self, value):
        self.value = value

    @classmethod
    def foo_0(cls):
        return cls(0)

    @staticmethod
    def mult(self):
        return self.value * 2


pop_case = {
    0: 'a',
    1: 'b',
    2: 'c'
}

for e in pop_case:
    print(e, pop_case[e])
