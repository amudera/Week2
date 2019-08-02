import gameboard 
from gameboard import Gameplay
plays = Gameplay()

def playgame():
    plays.opening()
    plays.random_cords()
    while True:
        attempts = plays.attempts()
        plays.play(attempts)

playgame()
    