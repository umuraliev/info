class iter_int(int):
    def __init__(self, val):
        self.val = val

    def __iter__(self):
        num = self.val
        for s in str(num):
            if s == '.' or s == '-':
                yield s
            else:
                yield int(s)

    def __add__(self, other): return iter_int(self.val + other)
    def __sub__(self, other): return iter_int(self.val - other)    
    def __mul__(self, other): return iter_int(self.val * other)
    def __truediv__(self, other): return iter_int(self.val / other)
    def __floordiv__(self, other): return iter_int(self.val // other)
    def __radd__(self, other): return iter_int(other + self.val)
    def __rsub__(self, other): return iter_int(other - self.val)
    def __rmul__(self, other): return iter_int(other * self.val)
    def __rtruediv__(self, other): return iter_int(other / self.val)
    def __rfloordiv__(self, other): return iter_int(other // self.val)

res = iter_int(4444.04)/4

for i in res:
    print(i)
