class InfiniteRange:
    """Класс обеспечивает бесконечное последовательное возведение в квадрат заданного числа."""
    def __init__(self, initial_number):
        # Здесь хранится промежуточное значение
        self.number_to_square = initial_number

    def __next__(self):
        import time
        # Здесь мы обновляем значение и возвращаем результат
        self.number_to_square += 1
        return self.number_to_square

    def __iter__(self):
        """Этот метод позволяет при передаче объекта функции iter возвращать самого себя, тем самым в точности реализуя протокол итератора."""
        return self

for i in InfiniteRange(2):
    print(i)