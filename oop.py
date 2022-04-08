"""
OOП - Обьектно ориентированное программирование (парадигма)
"""

# Принципы ООП
"Основные"
# 1. - Наследование
# 1.2 - Множественное наследование
# 2. - Полиморфизм
# 3. - Инкапсуляция
"Доп"
# 1. - Абстракция
# 2. - Ассоциация
# 2.1 - Агрегация
# 2.2 - Композиция

"""
Наследование - принцип ООП, где мы можем в дочернем классе унаследовать, переопределять и использовать все методы и аттрибуты родительского класса
"""
class A:
    def method1(self):
        """Этот метод выводит строку"""
        print("method1 in class A")

class B(A):
    """Наследовали все методы и аттрибуты у класса А"""

b = B() # Создали обьект (экземпляр) от класса В
b.method1() # Можем вызвать метод method1, который был создан в классе А



"""
Полиморфизм - принцип ООП, где мы можем создавать в разных классах одноименные методы и аттрибуты с разным функционалом
"""
class A:
    def __str__(self) -> str:
        """
        метод __str__ работает, когда:
        1. мы оборачиваем обьект в str -> str(A())
        2. принтим обьект -> print(A())
        """
        return "A object"

class B:
    def __str__(self):
        return "B object"

print(A()) # 'A object' 
print(B()) # 'B object'
print(A()) # 'A object' 
print(A()) # 'A object' 
print(B()) # 'B object'



"""
Инкапсуляция - принцип ООП, где мы можем делать атрибуты и методы с разным уровнем доступа
"""
class A:
    attribute1 = "публичный аттрибут"
    _attribute2 = "защищенный аттрибут"
    __attribute3 = "приватный аттрибут (но можно обратиться так: _A__attribute3)"

    def method1(self):
        return "публичный метод"
    
    def _method2(self):
        return "защищенный метод"
    
    def __method3(self):
        # self.__attribute3 -> все ок
        return "приватный метод (_A__method3)"

# A().__attribute3 -> AttributeError
# A()._A__attribute3 -> "приватный аттрибут (но можно обратиться так: _A__attribute3)"

"""Getters and Setters"""
# это методы, через которые мы можем получать (getter)  и изменять (setter) значения защищенных и приватных аттрибутов

class A:
    _attr1 = "защищенный аттрибут"
    __attr2 = "приватный аттрибут"

    def get_attr1(self):
        """Возвращает значение аттрибута _attr1"""
        return self._attr1

    def get_attr2(self):
        """Возвращает значение аттрибута __attr2"""
        return self.__attr2
    
    def set_attr1(self, value):
        """Меняет значение _attr1"""
        self._attr1 = value

    def set_attr2(self, value):
        """Меняет значение __attr2"""
        self.__attr2 = value

a = A()
print(a.get_attr1(), a.get_attr2())
a.set_attr1("New val")
a.set_attr2("Val")
print(a.get_attr1(), a.get_attr2())



"""
Множественное наследование - принцип ООП, в тором мы наследуем все аттрибуты и методы у всех родителей
"""
class A:
    def method_a(self):
        ...

class B: 
    def method_b(self):
        ...

class C(A,B):
    """
    Класс унаследовал все аттрибуты и методы класса А и класса В и все аттрибуты и методы их родителей (object)
    """

c = C()
c.method_a()
c.method_b()


"""Проблемы множественного наследования"""
# 1. - Проблема ромба (решена через mro)
# 2. - Проблема перекрестного наследования (не решена)


"""Проблема ромба"""
class A:
    """корневой класс"""

    def method_a(self):
        return "A"

class B(A):
    """Первый дочерний класс от А"""

    def method_b(self):
        return "B"

class C(A):
    """Второй дочерний класс от А"""

    def method_c(self):
        return "C"

class D(B,C):
    """Дочерний класс от В и С"""
    
    def method_d(self):
        return "D"

d = D()
d.method_a()
d.method_b()
d.method_c()
d.method_d()

# MRO - D -> B -> C -> A 

"""Проблема перекрестного наследования"""

# class A: ...
# class B: ...

# class C(A,B): ...
# class D(B,A): ...

# class E(C,D): ... -> Error
"""
    class E(C,D): ...
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, B
"""