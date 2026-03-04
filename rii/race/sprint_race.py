from race.race import Race


class SprintRace(Race):
    def startLine(self, track):
        print("Sprint race started at starting line")

    def finishLine(self, track):
        print("Sprint race finished at end of track")