from tracks.blue_moon import BlueMoon
from tracks.bb_raceway import BBRaceway
from tracks.spa import Spa

class TrackFactory:

    @staticmethod
    def get_track(choice):
        choice = choice.lower()
        if choice == "bluemoon":
            return BlueMoon()
        elif choice == "bbraceway":
            return BBRaceway()
        elif choice == "spa":
            return Spa()
        return None
