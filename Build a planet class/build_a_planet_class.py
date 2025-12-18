class Planet:
    def __init__(self, name, planet_type, star):
        # Type check
        if not all(isinstance(arg, str) for arg in (name, planet_type, star)):
            raise TypeError("name, planet type, and star must be strings")

        # Empty string check
        if not all(arg.strip() for arg in (name, planet_type, star)):
            raise ValueError("name, planet_type, and star must be non-empty strings")

        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


# Creating planet instances
planet_1 = Planet("Earth", "Terrestrial", "Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "Sun")
planet_3 = Planet("Kepler-452b", "Super-Earth", "Kepler-452")

# Printing planet objects (__str__ method)
print(planet_1)
print(planet_2)
print(planet_3)

# Calling orbit method and printing results
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
