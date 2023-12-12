class Main:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def summa(self):
        return self.a + self.b


result = Main(5, 8)
print(result.summa())
