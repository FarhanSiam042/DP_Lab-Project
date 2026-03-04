from cars.toyota import ToyotaGR86
from cars.subaru import SubaruBRZ
from cars.porsche import PorscheBoxster
from cars.ferrari import Ferrari812

class CarFactory:

    @staticmethod
    def get_car(choice):
        choice = choice.lower()
        if choice == "toyota":
            return ToyotaGR86()
        elif choice == "subaru":
            return SubaruBRZ()
        elif choice == "porsche":
            return PorscheBoxster()
        elif choice == "ferrari":
            return Ferrari812()
        return None
