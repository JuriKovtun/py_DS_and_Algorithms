class Foo():
    def __init__(self, value):
        self.value = value

    @classmethod
    def foo_0(cls):
        return cls(0)

    @staticmethod
    def mult(self):
        return self.value * 2
