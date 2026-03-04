class CarDecorator:
    def __init__(self, car):
        self.car = car

    def start(self):
        self.car.start()

    def accelerate(self):
        self.car.accelerate()

    def stop(self):
        self.car.stop()

    def carInfo(self):
        self.car.carInfo()

        