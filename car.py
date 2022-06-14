class Car():
    speed: int = 0
    pos: int = 0

    def __init__(self, speed: int):
        self.speed = speed

    def start(self) -> None:
        self.pos = 0

    def move(self) -> None:
        self.pos += self.speed


def main(args=None) -> None:
    car_list = list()
    N = int(input())
    for i in range(N):
        speed = int(input())
        car_list.append(Car(speed))

    loop_count = int(input())
    for car in car_list:
        # それぞれの車を取り出す
        for t in range(loop_count):
            # M時間車をそれぞれ進める
            car.move()

    over_100km_cars: int = 0
    for car in car_list:
        if car.pos > 100:
            over_100km_cars += 1

    print(over_100km_cars)


if __name__ == "__main__":
    main()
