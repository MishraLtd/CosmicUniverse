def update(rocket,engine, gravity, dt):
    mass = rocket.dry_mass + rocket.fuel_mass
    
    weight = mass * gravity

    drag = 0.4

    net_force = engine.thrust - weight - drag

    acceleration = net_force/mass
    

    #updated velocity
    rocket.velocity = rocket.velocity + acceleration * dt

    #update altitude
    rocket.altitude = rocket.altitude + rocket.velocity * dt
    if rocket.altitude < 0:
        rocket.altitude = 0
        rocket.velocity = 0


    #Burn Rate
    rocket.fuel_mass -= engine.burn_rate * dt

    #Burn Rate Backfire

    if rocket.fuel_mass <0:
        rocket.fuel_mass= 0


    

