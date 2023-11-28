'''
імпортує класи з файлу lab5
'''
from lab5 import Planet, PlanetType, Planetary

def print_planet_parametrs():
    '''
    виводить значення про планети
    '''
    planet1 = Planet("Земля", 16, 1000, 30, 24, 9, PlanetType.TERRESTRIAL)
    planet2 = Planet("Марс", 12, 2000, 10, 20, 1, PlanetType.JOVIAN)
    planet3 = Planet("Юпітер", 8, 1500, 2, 26, 7, PlanetType.TERRESTRIAL)

    planetary = Planetary()
    planetary.add_planet(planet1)
    planetary.add_planet(planet2)
    planetary.add_planet(planet3)

    print(planetary.find_distance_between(planet1, planet3))

    print(planetary.find_average_mass())

    print(planetary.sort_by_length_of_day())

if __name__ == "__main__":
    print_planet_parametrs()
