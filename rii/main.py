from player import Player
from factories.car_factory import CarFactory
from factories.track_factory import TrackFactory
from strategy.engine_strategy import V6, V8, V12
from strategy.turbo_strategy import Alpine, Cummins, Honeywell
from race.sprint_race import SprintRace
from race.circuit_race import CircuitRace
from decorator.SemaNOS import SemaNOS
from decorator.ResonacNOS import ResonacNOS

name = input("Enter Player Name: ")
player = Player(name)

car_choice = input("Choose Car: ")
car = CarFactory.get_car(car_choice)

engine = V8()
turbo = Alpine()

car.set_engine(engine)
car.set_turbo(turbo)

# Apply NOS decorator
nos_choice = input("Add NOS boost? (Sema/Resonac/None): ").lower()
if nos_choice == "sema":
    car = SemaNOS(car)
    print("Sema NOS installed!")
elif nos_choice == "resonac":
    car = ResonacNOS(car)
    print("Resonac NOS installed!")

track_choice = input("Choose Track: ")
track = TrackFactory.get_track(track_choice)

race_type = input("Choose Race Type (Sprint/Circuit): ")

if race_type == "Sprint":
    race = SprintRace()
else:
    race = CircuitRace()

race.race(car, track)
race.race(car, track)