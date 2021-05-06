import time
class TrafficLight:
    color = 'green'
    def color_green(self):
        color = 'green'
        print('Зеленый')
        return color

    def color_yellow(self):
        color = 'yellow'
        print('Желтый')
        return color

    def color_rad(self):
        color = 'red'
        print('Красный')
        return color

TrafficLight_1 = TrafficLight()
while True:
    TrafficLight_1.color_green()
    time.sleep(7)
    TrafficLight_1.color_yellow()
    time.sleep(2)
    TrafficLight_1.color_rad()
    time.sleep(7)
    TrafficLight_1.color_yellow()
    time.sleep(2)
