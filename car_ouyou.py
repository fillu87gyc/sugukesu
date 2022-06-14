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

    move_list: list = list(map(int, input().split(',')))

    for move_car_number in move_list:
        car_list[move_car_number].move()

    for car in car_list:
        print(car.pos)


if __name__ == "__main__":
    main()
