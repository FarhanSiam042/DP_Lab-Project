from tracks.track import Track


class BBRaceway(Track):
    def __init__(self):
        super().__init__("BB Raceway", 2.8, "Japan")

    def trackInfo(self):
        print(f"Track: {self.name} ({self.country}) - Length: {self.length} km")
