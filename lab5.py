'''
Імпортує клас енам
'''


from enum import Enum


class PlanetType(Enum):
    '''
    Клас по визначенню типу планети
    '''
    TERRESTRIAL = 1
    JOVIAN = 2


class Planet:
    '''
    Клас який містить дані про планету
    '''
    def __init__(self, name, kg, speed, degree, hour, kilometres, planet_type):
        '''
        Функція яка ініціалізує початкові значення
        '''
        self.name = name
        self.mass = kg
        self.orbital_velosity = speed
        self.mean_temparature = degree
        self.length_of_day = hour
        self.distance_from_sun = kilometres
        self.type = planet_type


    def find_mass(self):
        '''
        Виводить масу планети
        '''
        return f"Маса планети {self.name}: {self.mass}"


    def find_mean_temparature(self):
        '''
        Виводить температуру планети
        '''
        return f"Температура планети {self.name}: {self.mean_temparature}"


class Planetary():
    '''
    Клас який містить планети
    '''
    def __init__(self):
        '''
        Функція яка ініціалізує планети
        '''
        self.planets = []

    def add_planet(self, planet):
        '''
        Функція яка додає планети
        '''
        self.planets.append(planet)

    def sort_by_length_of_day(self):
        '''
        Функція яка сортує планети за довжиною дня
        '''
        self.planets.sort(key=lambda x: x.length_of_day)
        for i in self.planets:
           return f"Назва планети: {i.name}, Довжина світлового дня: {i.length_of_day}"


    def find_distance_between(self, planet_a, planet_b):
        '''
        Фунція яка шукаю відстань між планетами
        '''
        return abs(planet_a.distance_from_sun - planet_b.distance_from_sun)


    def find_average_mass(self):
        '''
        Функція яка шукаю середню масу всіх планет
        '''
        total_mass = sum(planet.mass for planet in self.planets)
        return total_mass / len(self.planets)
    