class Planet:  # Конструкторний клас для планет
    def __init__(self, name, mass, radius, rotation_period, orbital_period, distance_from_sun, planet_type,
                 surface_temperature, degree, number_of_moons, atmosphere, satellite):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type
        self.surface_temperature = surface_temperature
        self.degree = degree
        self.number_of_moons = number_of_moons
        self.atmosphere = atmosphere
        self.satellite = satellite


class Atmosphere:  # Конструкторний клас для атмосфер
    def __init__(self, composition, layer_thickness, temperature, density, surface_pressure, wind_speed,
                 has_ozone_layer, greenhouse_gas_concentration, has_magnetic_field, troposphere_height):
        self.composition = composition
        self.layer_thickness = layer_thickness
        self.temperature = temperature
        self.density = density
        self.surface_pressure = surface_pressure
        self.wind_speed = wind_speed
        self.has_ozone_layer = has_ozone_layer
        self.greenhouse_gas_concentration = greenhouse_gas_concentration
        self.has_magnetic_field = has_magnetic_field
        self.troposphere_height = troposphere_height


class Star:  # Конструкторний клас для зірок
    def __init__(self, name, star_type, mass, surface_temperature, radius, luminosity, age, metallicity,
                 solar_activity_frequency, rotation_period):
        self.name = name
        self.star_type = star_type
        self.mass = mass
        self.surface_temperature = surface_temperature
        self.radius = radius
        self.luminosity = luminosity
        self.age = age
        self.metallicity = metallicity
        self.solar_activity_frequency = solar_activity_frequency
        self.rotation_period = rotation_period


class Satellite:  # Конструкторний клас для супутників
    def __init__(self, name, orbit_radius, mass, orbital_period, surface_temperature, satellite_type, parent_planet,
                 age, atmosphere_present, distance_from_parent_planet):
        self.name = name
        self.orbit_radius = orbit_radius
        self.mass = mass
        self.orbital_period = orbital_period
        self.surface_temperature = surface_temperature
        self.satellite_type = satellite_type
        self.parent_planet = parent_planet
        self.age = age
        self.atmosphere_present = atmosphere_present
        self.distance_from_parent_planet = distance_from_parent_planet


class SolarSystem:  # Конструкторний клас для систем
    def __init__(self, name, star, number_of_planets, asteroid_belt, total_mass, system_radius, has_comets,
                 nearby_black_holes, galactic_orbit_speed, age):
        self.name = name
        self.star = star
        self.number_of_planets = number_of_planets
        self.asteroid_belt = asteroid_belt
        self.total_mass = total_mass
        self.system_radius = system_radius
        self.has_comets = has_comets
        self.nearby_black_holes = nearby_black_holes
        self.galactic_orbit_speed = galactic_orbit_speed
        self.age = age


# Створюю супутники
Moon = Satellite("Місяць", 384400, "7.34 × 10²² кг", 27.3, -53, "твердий", "Земля", 4.5, False, 0.384)
Europa = Satellite("Європа", 670900, "4.80 × 10²² кг", 3.5, -160, "лідний", "Юпітер", 4.5, True, 0.628)
Titan = Satellite("Титан", 1221700, "1.35 × 10²³ кг", 15.9, -179, "газовий", "Сатурн", 4.5, True, 1.222)

# Створюю атмосфери
EarthAtmosphere = Atmosphere("Азот (78%), Кисень (21%), Інші гази (1%)", 100, 15, 1.225, 101.3, 10, True, 0.04, True,
                             12)
VenusAtmosphere = Atmosphere("Вуглекислий газ (96.5%), Азот (3.5%)", 250, 465, 65, 9200, 100, False, 96.5, False, 70)
MarsAtmosphere = Atmosphere("Вуглекислий газ (95%), Аргон (1.6%), Азот (2.7%)", 80, -60, 0.020, 0.636, 5, False, 95,
                            False, 40)
# Створюю планети
Mercury = Planet("Меркурій", "3.3011 × 10²³ кг", 2439.7, 58.6, 88, 57.9, "Скеляста", 167, 0, 0, EarthAtmosphere, Moon)
Venus = Planet("Венера", "4.8675 × 10²⁴ кг", 6051.8, 243, 225, 108.2, "Скеляста", 465, 177.4, 0, VenusAtmosphere, None)
Earth = Planet("Земля", "5.972 × 10²⁴ кг", 6371, 24, 365, 149.6, "Скеляста", 15, 23.5, 1, MarsAtmosphere, None)

# Створюю зірки
Sun = Star("Сонце", "жовтий карлик", "1.989 × 10²⁴ кг", 5778, 695700, "3.828 × 10²⁶ Вт", 4.6, 0.02, 11, 25)
Sirius = Star("Сіріус", "біла", "2.0 × 10²⁴ кг", 9940, 1189600, "25.4 × 10²⁶ Вт", 0.2, 0.1, 16, 10)
Betelgeuse = Star("Бетельгейзе", "червоний гігант", "1.5 × 10²⁵ кг", 3500, 887000, "1.2 × 10²⁷ Вт", 10, 0.5, 12, 30)

# Створюю різні системи.
SolarSystemMilkyWay = SolarSystem("Сонячна система", "Сонце", 8, True, "1.0 × 10²⁴ кг", "1.0 × 10¹⁴ км", True, 1,
                                  "828,000 км/год", 4.6)
SolarSystemAlphaCentauri = SolarSystem("Альфа Центавра", "Альфа Центавра A", 3, False, "2.0 × 10²⁴ кг", "1.2 × 10¹⁴ км",
                                       False, 0, "760,000 км/год", 5.0)
SolarSystemThetaCassiopeiae = SolarSystem("Тета Касіопеї", "Тета Касіопеї", 5, True, "1.5 × 10²⁴ кг", "1.5 × 10¹⁴ км",
                                          True, 1, "800,000 км/год", 6.0)
# Вивід всіх даних
print(f"Імʼя планети: {Mercury.name}"
      f"\nМаса: {Mercury.mass}"
      f"\nРадіус: {Mercury.radius}"
      f"\nПеріод оберту навколо осі: {Mercury.rotation_period}"
      f"\nПеріод оберту навколо Сонця: {Mercury.orbital_period}"
      f"\nВідстань до Сонця: {Mercury.distance_from_sun}"
      f"\nТип планети: {Mercury.planet_type}"
      f"\nТемпература на поверхні: {Mercury.surface_temperature}"
      f"\nНахил осі: {Mercury.degree}\nКількість супутників: {Mercury.number_of_moons}"
      f"\n"
      f"\nІмʼя планети: {Venus.name}"
      f"\nМаса: {Venus.mass}"
      f"\nРадіус: {Venus.radius}"
      f"\nПеріод оберту навколо осі: {Venus.rotation_period}"
      f"\nПеріод оберту навколо Сонця: {Venus.orbital_period}"
      f"\nВідстань до Сонця: {Venus.distance_from_sun}"
      f"\nТип планети: {Venus.planet_type}"
      f"\nТемпература на поверхні: {Venus.surface_temperature}"
      f"\nНахил осі: {Venus.degree}\nКількість супутників: {Venus.number_of_moons}"
      f"\n"
      f"\nІмʼя планети: {Earth.name}"
      f"\nМаса: {Earth.mass}"
      f"\nРадіус: {Earth.radius}"
      f"\nПеріод оберту навколо осі: {Earth.rotation_period}"
      f"\nПеріод оберту навколо Сонця: {Earth.orbital_period}"
      f"\nВідстань до Сонця: {Earth.distance_from_sun}"
      f"\nТип планети: {Earth.planet_type}"
      f"\nТемпература на поверхні: {Earth.surface_temperature}"
      f"\nНахил осі: {Earth.degree}"
      f"\nКількість супутників: {Earth.number_of_moons}"
      f"\n"
      f"\nІмʼя атмосфери: Земля"
      f"\nСклад: {EarthAtmosphere.composition}"
      f"\nТовщина шару атмосфери: {EarthAtmosphere.layer_thickness} км"
      f"\nТемпература: {EarthAtmosphere.temperature} °C"
      f"\nЩільність: {EarthAtmosphere.density} кг/м³"
      f"\nАтмосферний тиск на поверхні: {EarthAtmosphere.surface_pressure} кПа"
      f"\nШвидкість вітрів: {EarthAtmosphere.wind_speed} м/с"
      f"\nНаявність озонового шару: {EarthAtmosphere.has_ozone_layer}"
      f"\nКонцентрація парникових газів: {EarthAtmosphere.greenhouse_gas_concentration}%"
      f"\nНаявність магнітного поля: {EarthAtmosphere.has_magnetic_field}"
      f"\nВисота тропосфери: {EarthAtmosphere.troposphere_height} км"
      f"\n"
      f"\nІмʼя атмосфери: Венера"
      f"\nСклад: {VenusAtmosphere.composition}"
      f"\nТовщина шару атмосфери: {VenusAtmosphere.layer_thickness} км"
      f"\nТемпература: {VenusAtmosphere.temperature} °C"
      f"\nЩільність: {VenusAtmosphere.density} кг/м³"
      f"\nАтмосферний тиск на поверхні: {VenusAtmosphere.surface_pressure} кПа"
      f"\nШвидкість вітрів: {VenusAtmosphere.wind_speed} м/с"
      f"\nНаявність озонового шару: {VenusAtmosphere.has_ozone_layer}"
      f"\nКонцентрація парникових газів: {VenusAtmosphere.greenhouse_gas_concentration}%"
      f"\nНаявність магнітного поля: {VenusAtmosphere.has_magnetic_field}"
      f"\nВисота тропосфери: {VenusAtmosphere.troposphere_height} км"
      f"\n"
      f"\nІмʼя атмосфери: Марс"
      f"\nСклад: {MarsAtmosphere.composition}"
      f"\nТовщина шару атмосфери: {MarsAtmosphere.layer_thickness} км"
      f"\nТемпература: {MarsAtmosphere.temperature} °C"
      f"\nЩільність: {MarsAtmosphere.density} кг/м³"
      f"\nАтмосферний тиск на поверхні: {MarsAtmosphere.surface_pressure} кПа"
      f"\nШвидкість вітрів: {MarsAtmosphere.wind_speed} м/с"
      f"\nНаявність озонового шару: {MarsAtmosphere.has_ozone_layer}"
      f"\nКонцентрація парникових газів: {MarsAtmosphere.greenhouse_gas_concentration}%"
      f"\nНаявність магнітного поля: {MarsAtmosphere.has_magnetic_field}"
      f"\nВисота тропосфери: {MarsAtmosphere.troposphere_height} км"
      f"\n"
      f"\nІмʼя зірки: {Sun.name}"
      f"\nТип зірки: {Sun.star_type}"
      f"\nМаса: {Sun.mass}"
      f"\nТемпература поверхні: {Sun.surface_temperature} K"
      f"\nРадіус: {Sun.radius} км"
      f"\nСвітність: {Sun.luminosity}"
      f"\nВік: {Sun.age} млрд років"
      f"\nМеталічність: {Sun.metallicity}"
      f"\nЧастота сонячної активності: {Sun.solar_activity_frequency} циклів на рік"
      f"\nПеріод обертання: {Sun.rotation_period} днів"
      f"\n"
      f"\nІмʼя зірки: {Sirius.name}"
      f"\nТип зірки: {Sirius.star_type}"
      f"\nМаса: {Sirius.mass}"
      f"\nТемпература поверхні: {Sirius.surface_temperature} K"
      f"\nРадіус: {Sirius.radius} км"
      f"\nСвітність: {Sirius.luminosity}"
      f"\nВік: {Sirius.age} млрд років"
      f"\nМеталічність: {Sirius.metallicity}"
      f"\nЧастота сонячної активності: {Sirius.solar_activity_frequency} циклів на рік"
      f"\nПеріод обертання: {Sirius.rotation_period} днів"
      f"\n"
      f"\nІмʼя зірки: {Betelgeuse.name}"
      f"\nТип зірки: {Betelgeuse.star_type}"
      f"\nМаса: {Betelgeuse.mass}"
      f"\nТемпература поверхні: {Betelgeuse.surface_temperature} K"
      f"\nРадіус: {Betelgeuse.radius} км"
      f"\nСвітність: {Betelgeuse.luminosity}"
      f"\nВік: {Betelgeuse.age} млрд років"
      f"\nМеталічність: {Betelgeuse.metallicity}"
      f"\nЧастота сонячної активності: {Betelgeuse.solar_activity_frequency} циклів на рік"
      f"\nПеріод обертання: {Betelgeuse.rotation_period} днів"
      f"\n"
      f"\nІмʼя: {Moon.name}"
      f"\nРадіус орбіти: {Moon.orbit_radius}"
      f"\nМаса: {Moon.mass}"
      f"\nПеріод обертань: {Moon.orbital_period}"
      f"\nТемпература поверхні: {Moon.surface_temperature}"
      f"\nТип супутника: {Moon.satellite_type}"
      f"\nБатькова планета: {Moon.parent_planet}"
      f"\nВік: {Moon.age}"
      f"\nЧи наявна атмосфера? {Moon.atmosphere_present}"
      f"\nВідстань до батькової планети: {Moon.distance_from_parent_planet}"
      f"\n"
      f"\nІмʼя: {Europa.name}"
      f"\nРадіус орбіти: {Europa.orbit_radius}"
      f"\nМаса: {Europa.mass}"
      f"\nПеріод обертань: {Europa.orbital_period}"
      f"\nТемпература поверхні: {Europa.surface_temperature}"
      f"\nТип супутника: {Europa.satellite_type}"
      f"\nБатькова планета: {Europa.parent_planet}"
      f"\nВік: {Europa.age}"
      f"\nЧи наявна атмосфера? {Europa.atmosphere_present}"
      f"\nВідстань до батькової планети: {Europa.distance_from_parent_planet}"
      f"\n"
      f"\nІмʼя: {Titan.name}"
      f"\nРадіус орбіти: {Titan.orbit_radius}"
      f"\nМаса: {Titan.mass}"
      f"\nПеріод обертань: {Titan.orbital_period}"
      f"\nТемпература поверхні: {Titan.surface_temperature}"
      f"\nТип супутника: {Titan.satellite_type}"
      f"\nБатькова планета: {Titan.parent_planet}"
      f"\nВік: {Titan.age}"
      f"\nЧи наявна атмосфера? {Titan.atmosphere_present}"
      f"\nВідстань до батькової планети: {Titan.distance_from_parent_planet}"
      f"\n"
      f"\nІм'я: {SolarSystemMilkyWay.name}"
      f"\nЗірка: {SolarSystemMilkyWay.star}"
      f"\nКількість планет: {SolarSystemMilkyWay.number_of_planets}"
      f"\nЧи є астероїдний пояс? {SolarSystemMilkyWay.asteroid_belt}"
      f"\nЗагальна маса: {SolarSystemMilkyWay.total_mass}"
      f"\nРадіус системи: {SolarSystemMilkyWay.system_radius}"
      f"\nЧи є комети? {SolarSystemMilkyWay.has_comets}"
      f"\nСкільки поряд чорних дір? {SolarSystemMilkyWay.nearby_black_holes}"
      f"\nГалактична швидкість обертання: {SolarSystemMilkyWay.galactic_orbit_speed}"
      f"\nВік: {SolarSystemAlphaCentauri.age}"
      f"\n"
      f"\nІм'я: {SolarSystemAlphaCentauri.name}"
      f"\nЗірка: {SolarSystemAlphaCentauri.star}"
      f"\nКількість планет: {SolarSystemAlphaCentauri.number_of_planets}"
      f"\nЧи є астероїдний пояс? {SolarSystemAlphaCentauri.asteroid_belt}"
      f"\nЗагальна маса: {SolarSystemAlphaCentauri.total_mass}"
      f"\nРадіус системи: {SolarSystemAlphaCentauri.system_radius}"
      f"\nЧи є комети? {SolarSystemAlphaCentauri.has_comets}"
      f"\nСкільки поряд чорних дір? {SolarSystemAlphaCentauri.nearby_black_holes}"
      f"\nГалактична швидкість обертання: {SolarSystemAlphaCentauri.galactic_orbit_speed}"
      f"\nВік: {SolarSystemThetaCassiopeiae.age}"
      f"\n"
      f"\nІм'я: {SolarSystemThetaCassiopeiae.name}"
      f"\nЗірка: {SolarSystemThetaCassiopeiae.star}"
      f"\nКількість планет: {SolarSystemThetaCassiopeiae.number_of_planets}"
      f"\nЧи є астероїдний пояс? {SolarSystemThetaCassiopeiae.asteroid_belt}"
      f"\nЗагальна маса: {SolarSystemThetaCassiopeiae.total_mass}"
      f"\nРадіус системи: {SolarSystemThetaCassiopeiae.system_radius}"
      f"\nЧи є комети? {SolarSystemThetaCassiopeiae.has_comets}"
      f"\nСкільки поряд чорних дір? {SolarSystemThetaCassiopeiae.nearby_black_holes}"
      f"\nГалактична швидкість обертання: {SolarSystemThetaCassiopeiae.galactic_orbit_speed}"
      f"\nВік: {SolarSystemThetaCassiopeiae.age}")
