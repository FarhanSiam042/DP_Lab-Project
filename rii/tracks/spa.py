from tracks.track import Track


class Spa(Track):
    def __init__(self):
        super().__init__("Spa-Francorchamps", 7.0)

    def trackInfo(self):
        print(f"Track: {self.name} - Length: {self.length} km")
