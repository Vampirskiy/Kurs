class Road:
    __v = 25
    def ves(self, _a, _l, _h):
        print(f'Вес покрытия: {int(_a) * int(_l) * self.__v * int(_h)} тон')

Road_1 = Road()
z = input(' Введите параметры: ширина(м), длина(м), толщина(см):  ').split(' ')
[_a, _l, _h] = z
Road_1.ves(_a, _l, _h)
