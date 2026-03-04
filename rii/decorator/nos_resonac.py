from decorator.car_decorator import CarDecorator


class NOSResonac(CarDecorator):
    def accelerate(self):
        super().accelerate()
        print("NOS Resonac boost activated!")

    def carInfo(self):
        super().carInfo()
        print("+ NOS Resonac equipped")
