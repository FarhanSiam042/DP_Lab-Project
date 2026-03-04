import random
import datetime

class Race:

    def race(self, car, track):

        car.carInfo()
        track.trackInfo()

        self.startCar(car)
        self.startLine(track)
        self.accelerateCar(car)

        car = self.pitStop(car)
        self.finishLine(track)
        self.stopCar(car)
        self.lapTime()

    def startCar(self, car):
        car.start()

    def accelerateCar(self, car):
        car.accelerate()

    def stopCar(self, car):
        car.stop()

    def lapTime(self):
        seconds = random.randint(60, 500)
        time = str(datetime.timedelta(seconds=seconds))
        print("Lap Time:", time)

    def startLine(self, track):
        pass

    def finishLine(self, track):
        pass

    def pitStop(self, car):
        return car