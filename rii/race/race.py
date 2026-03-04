import random
import datetime
from decorator.SemaNOS import SemaNOS
from decorator.ResonacNOS import ResonacNOS


class Race:

    def race(self, car, track):
        """Template method - defines the race flow"""
        # Step a) Car.carInfo()
        car.carInfo()
        
        # Step b) Track.trackInfo()
        track.trackInfo()
        
        # Step c) startCar(Car)
        self.startCar(car)
        
        # Step d) startLine(Track)
        self.startLine(track)
        
        # Step e) accelerateCar(Car)
        self.accelerateCar(car)
        
        # Step f) NOS = pitStop(Car)
        car = self.pitStop(car)
        
        # Step g) applyNos(NOS)
        self.applyNos(car)
        
        # Step h) finishLine(Track)
        self.finishLine(track)
        
        # Step i) stopCar(NOS)
        self.stopCar(car)
        
        # Step j) lapTime()
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
        """Ask player if they want to apply NOS"""
        print("\n--- PIT STOP ---")
        nos_choice = input("Apply NOS? (Sema/Resonac/None): ").lower()
        
        if nos_choice == "sema":
            print("Installing Sema NOS...")
            car = SemaNOS(car)
        elif nos_choice == "resonac":
            print("Installing Resonac NOS...")
            car = ResonacNOS(car)
        
        return car

    def applyNos(self, car):
        """Apply NOS boost if present (triggers accelerate on decorated car)"""
        if hasattr(car, 'car'):  # Check if it's a decorator wrapping a car
            print("Applying NOS boost!")
            # The decorator's accelerate already prints the boost message
