class Person:
    def __init__(self, name, age) -> None:
        self.name=name
        self.age=age

    def __str__(self) -> str:
        return f'{self.name} ({self.age})'

    def introfunc(self):
        print(f'Hello, I am {self.name} and I am {self.age} years old')
p1=Person('Thomas', 26)
print(p1.name)
print(p1.age)
print(p1)
p1.age = 30
p1.introfunc()
# del p1.age
# del p1
# print(p1)
class Empty:
    pass
