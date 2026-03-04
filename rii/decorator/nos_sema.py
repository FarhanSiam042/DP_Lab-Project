from decorator.car_decorator import CarDecorator


class NOSSema(CarDecorator):
    def accelerate(self):
        super().accelerate()
        print("NOS Sema boost activated!")

    def carInfo(self):
        super().carInfo()
        print("+ NOS Sema equipped")
