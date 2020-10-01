'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод
'''
class TrafficLight:

    #атрибут класса
    traffic_light_color = "red"
    time = 0

    #метод класса
    def on_traffic_light_running(self):
        self.time += 1
        if self.time % 12 == 7:
            self.traffic_light_color = "yellow"
        elif self.time % 12 == 9:
            self.traffic_light_color = "green"
        elif self.time % 12 == 0:
            self.traffic_light_color = "red"

t = TrafficLight()
for time in range(100):
    print(t.traffic_light_color)
    t.on_traffic_light_running()







