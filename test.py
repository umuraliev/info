class iter_int(int):
    def __iter__(self):
        num = self.real
        for i in str(num):
            yield int(i)
    
    def __getitem__(self, slice):
        for i, obj in enumerate(self):
            if i == slice:
                return obj
        raise IndexError
                
num = iter_int(553452)
for i in num:
    print(i)

print(num[5])


