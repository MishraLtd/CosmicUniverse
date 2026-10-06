from rocket import Rocket
from physics import update
from engine import Engine
from dashboard import display
import os
import time as tm

time = 0
dt = 0.1
gravity = 9.81
rocket = Rocket()
engine = Engine()

while rocket.fuel_mass > 0:
    update(rocket,engine,gravity,dt)
    time += dt
    os.system("clear")
    display(time,rocket,engine, gravity)
    tm.sleep(0.1)