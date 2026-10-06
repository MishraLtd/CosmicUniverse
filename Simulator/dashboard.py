def display(time, rocket, engine, gravity):
    print("==============================")
    print("      ROCKET DASHBOARD")

    print("-----------------------")
    print(f"Mission Time  : {time:.3f} s")
    print(f"Altitude : {rocket.altitude:.2f} m")

    print(f"Velocity : {rocket.velocity:.2f} m/s")

    print(f"Fuel : {rocket.fuel_mass:.2f} kg")

    print(f"Thrust : {engine.thrust} N")
