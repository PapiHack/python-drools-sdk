class Person:
    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get('name', 'John')
        self.age = kwargs.get('age', 46)
        self.id = kwargs.get('id', None)
        self.isMajor = kwargs.get('isMajor', None)

    def __str__(self) -> str:
        return 'Person [id => {}, name => {}, age => {}, isMajor => {}]'.format(self.id, self.name, self.age, self.isMajor)

person = Person(id=1)
P1 = Person(name='Fatou', id=2, age=15)
P2 = Person(name='Daba', id=3, age=17)
P3 = Person(name='Nabou', id=4, age=28)
persons = [P1, P2, P3]