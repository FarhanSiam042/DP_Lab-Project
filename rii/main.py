from player import Player
from factories.car_factory import CarFactory
from factories.track_factory import TrackFactory
from strategy.engine_strategy import V6, V8, V12
from strategy.turbo_strategy import Alpine, Cummins, Honeywell
from race.sprint_race import SprintRace
from race.circuit_race import CircuitRace

# Singleton Player instance
name = input("Enter Player Name: ")
player = Player(name)

# car using factory
car_choice = input("Choose Car (Toyota/Subaru/Porsche/Ferrari): ")
car = CarFactory.get_car(car_choice)

# Set engine and turbo strategies
engine = V8()
turbo = Alpine()
car.set_engine(engine)
car.set_turbo(turbo)

# track using factory
track_choice = input("Choose Track (BlueMoon/BBRaceway/Spa): ")
track = TrackFactory.get_track(track_choice)

# race type
race_type = input("Choose Race Type (Sprint/Circuit): ").lower()

if race_type == "sprint":
    race = SprintRace()
else:
    race = CircuitRace()

# Execute race (NOS selection happens during pitStop in the race)
race.race(car, track)

