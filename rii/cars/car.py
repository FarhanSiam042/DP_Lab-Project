class Car:
    def __init__(self):
        self.engine = None
        self.turbo = None

    def set_engine(self, engine):
        self.engine = engine

    def set_turbo(self, turbo):
        self.turbo = turbo

    def start(self):
        print("Car started")

    def accelerate(self):
        print("Car accelerating")
        self.engine.run_engine()
        self.turbo.activate_turbo()

    def stop(self):
        print("Car stopped")

    def carInfo(self):
        pass