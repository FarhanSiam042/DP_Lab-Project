from decorator.car_decorator import CarDecorator


class ResonacNOS(CarDecorator):
    def accelerate(self):
        self.car.accelerate()
        print("Resonac NOS activated!")

    def carInfo(self):
        self.car.carInfo()
        print("+ Resonac NOS equipped")
