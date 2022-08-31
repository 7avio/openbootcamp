from functools import reduce


class Operations:

    def sum(self, *args):
        return reduce((lambda x, y: x + y), args)

    def minus(self, *args):
        return reduce((lambda x, y: x - y), args)

    def mul(self, *args):
        return reduce((lambda x, y: x * y), args)

    def div(self, *args):
        return reduce((lambda x, y: float(x // y)), args)
