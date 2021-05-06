class Worker:
    _income = {'wage':20000, 'bonus':5000}
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def data(self):
        print(f'{self.position} {self.surname} {self.name} заработная плата {int(self._income["wage"]) + int(self._income["bonus"])}')

Worker_1 = Worker('Иван', 'Иванов', 'Охранник')
Worker_1.data()

Worker_2 = Worker('Сергей', 'Ефимов', 'Администратор')
Worker_2.data()

Worker_3 = Worker('Михаил', 'Мишустин', 'Кладовщик')
Worker_3.data()
