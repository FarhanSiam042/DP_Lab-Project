from tracks.track import Track


class Spa(Track):
    def __init__(self):
        super().__init__("Circuit de Spa-Francorchamps", 7.0, "Germany")

    def trackInfo(self):
        print(f"Track: {self.name} ({self.country}) - Length: {self.length} km")
