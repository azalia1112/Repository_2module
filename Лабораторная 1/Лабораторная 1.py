class Employee:
    def __init__(self, salary: int, name: str):
        if not isinstance(salary, int):
            raise TypeError('Зарплату указывать в int')
        self.salary = salary
        if not isinstance(name, str):
            raise TypeError('Имя сотрудника указывать в str')
        self.name = name

    def count_employee(self):
        print('Имя:{}, Зарплата:{}'.format(self.name, self.salary))
class Laptop:
    def __init__(self, color: str, brand: str, price: int):
        if not isinstance(color, str):
            raise TypeError('Тип аргумента неверный(')
        self.color = color
        if not isinstance(brand, str):
            raise TypeError('Тип аргумента бренд неверный(')
        self.brand = brand
        if not isinstance(price, int):
            raise TypeError ('Указать цену в str')
        if price < 0:
            raise ValueError('Цена должна быть больше 0')
        self.price = price
    def put_an_ad(self):
        print('Продаю ноутбук')
class DesperateHousewives:
    def __init__(self, name: str, age:int):
        if not isinstance(name, str):
            raise TypeError('Указать имя в str')
        self.name = name
        if not isinstance(age, int):
            raise TypeError('Указать возраст в int')
        if age < 0:
            raise ValueError('Возраст должен быть больше либо равен 0')
        self.age = age
    def who_is_he(self, name):
        print(format(self.name, self.age))
if __name__ == "__main__":
    emp1 = Employee(10000, 'Артём')
    laptop1 = Laptop('red', 'apple', 100000)
    person1 = DesperateHousewives('Gabriel', 32)
    import doctest
    doctest.testmod()
    pass




        # TODO Написать 3 класса с документацией и аннотацией типов


    # TODO работоспособность экземпляров класса проверить с помощью doctest

