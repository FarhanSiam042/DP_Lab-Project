class TurboStrategy:
    def activate_turbo(self):
        pass


class Alpine(TurboStrategy):
    def activate_turbo(self):
        print("Alpine turbo activated")


class Cummins(TurboStrategy):
    def activate_turbo(self):
        print("Cummins turbo activated")


class Honeywell(TurboStrategy):
    def activate_turbo(self):
        print("Honeywell turbo activated")