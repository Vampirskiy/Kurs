class car():
    def __init__(self, name, color, speed, is_polis):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_polis = is_polis

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, turn_to):
        print(f'Поворот на {turn_to} градусов')

    def show_speed(self, maxspeed):
        if self.speed > maxspeed:
            print('Превышение скорости!')

TownCar = car('Hyundai', 'blu', 70, False)
print(TownCar.name, TownCar.color, TownCar.speed)
TownCar.go()
TownCar.show_speed(60)
TownCar.stop()

SportCar = car('Porsche', 'rad', 250, False)
print(SportCar.name, SportCar.color, SportCar.speed)
SportCar.go()
SportCar.turn(90)

WorkCar = car('nissan', 'white', 35, False)
print(WorkCar.name, WorkCar.color, WorkCar.speed)
WorkCar.go()
WorkCar.show_speed(40)
WorkCar.turn(-45)

PoliceCar = car('nissan', 'white', 35, True)
print(PoliceCar.name, PoliceCar.color, PoliceCar.speed)
PoliceCar.go()
PoliceCar.turn(45)
PoliceCar.turn(-90)
PoliceCar.stop()
