class Foo():
    def __init__(self, value):
        self.value = value

    @classmethod
    def foo_0(cls):
        return cls(0)

    @staticmethod
    def mult(self):
        return self.value * 2


data = {
    'a': 1,
    'b': 2,
    'e': 5
}


def bar(a, b, e):
    print(a, b, e)


def barb(**kw):
    print(kw)


bar(**data)
barb(a=1, b=2, c='3')
