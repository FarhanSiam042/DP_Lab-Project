from cars.toyota import ToyotaGR86
from cars.subaru import SubaruBRZ
from cars.porsche import PorscheBoxster
from cars.ferrari import Ferrari812

class CarFactory:

    @staticmethod
    def get_car(choice):
        if choice == "Toyota":
            return ToyotaGR86()
        elif choice == "Subaru":
            return SubaruBRZ()
        elif choice == "Porsche":
            return PorscheBoxster()
        elif choice == "Ferrari":
            return Ferrari812()