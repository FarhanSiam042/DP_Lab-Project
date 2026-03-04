from tracks.track import Track


class BlueMoon(Track):
    def __init__(self):
        super().__init__("Blue Moon", 3.5)

    def trackInfo(self):
        print(f"Track: {self.name} - Length: {self.length} km")
