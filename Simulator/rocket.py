class Rocket:

    def __init__(self):
        self.altitude= 0.0
        self.velocity= 0.0
        self.acceleration= 0.0

        self.dry_mass=100.0
        self.fuel_mass=50.0


    @property
    def total_mass(self):
        return self.dry_mass + self.fuel_mass
