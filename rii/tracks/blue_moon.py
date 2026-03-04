from tracks.track import Track


class BlueMoon(Track):
    def __init__(self):
        super().__init__("Blue Moon Bay Speedway", 3.5, "USA")

    def trackInfo(self):
        print(f"Track: {self.name} ({self.country}) - Length: {self.length} km")
