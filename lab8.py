import random

class Planet:
    def __init__(self, name="Unnamed"):
        self.name = name
        self.mass = random.uniform(0.1, 100)
        self.radius = random.uniform(1000, 70000)
        self.distance_from_star = random.uniform(1, 1000)
        self.orbital_period = random.uniform(0.5, 500)
        self.gravity = random.uniform(0.1, 25.0)
        self.rotation_period = random.randint(10, 1000)
        self.moons = random.randint(0, 50)
        self.temperature = random.randint(-200, 500)
        self.surface_type = random.randint(1, 5)
        self.atmosphere_thickness = random.randint(1, 300)

    def info(self):
        surface_types = {1: "Скеляста",2: "Газоподібна",3: "Льодяна",4: "Воднева",5: "Змішана"}
        print((f"Планета {self.name}:\n"
               f"  Маса: {self.mass:.2f} одиниці\n"
               f"  Радіус: {self.radius:.2f} кілометрів\n"
               f"  Відстань до Сонця: {self.distance_from_star:.2f} мільйонів кілометрів\n"
               f"  Орбітальний період: {self.orbital_period:.2f} днів\n"
               f"  Період обертання: {self.rotation_period} годин\n"
               f"  Кількість супутників: {self.moons}\n"
               f"  Температура: {self.temperature} °C\n"
               f"  Тип поверхні: {surface_types[self.surface_type]}\n"
               f"  Товщина атмосфери: {self.atmosphere_thickness} км\n"
               f"  Гравітація: {self.gravity:.2f} м/с²\n"))

planet1 = Planet("Землеподібна")
planet2 = Planet("Якась")
planet3 = Planet("Планета 2")
planet4 = Planet("Мяукурій")
planet5 = Planet("Гавкурій")

planet1.info()
planet2.info()
planet3.info()
planet4.info()
planet5.info()

