from decorator.car_decorator import CarDecorator


class SemaNOS(CarDecorator):
    def accelerate(self):
        self.car.accelerate()
        print("Sema NOS activated!")

    def carInfo(self):
        self.car.carInfo()
        print("+ Sema NOS equipped")
