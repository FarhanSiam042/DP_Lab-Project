from tracks.blue_moon import BlueMoon
from tracks.bb_raceway import BBRaceway
from tracks.spa import Spa

class TrackFactory:

    @staticmethod
    def get_track(choice):
        if choice == "BlueMoon":
            return BlueMoon()
        elif choice == "BBRaceway":
            return BBRaceway()
        elif choice == "Spa":
            return Spa()