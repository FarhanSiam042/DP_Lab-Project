from race.race import Race


class CircuitRace(Race):
    def startLine(self, track):
        print("Circuit race started")

    def finishLine(self, track):
        print("Circuit race finished at starting point")