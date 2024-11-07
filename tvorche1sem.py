import random


class Client:
    def __init__(self, name, age, price, experience, health, profession):
        self.name = name
        self.age = age
        self.price = price
        self.experience = experience
        self.health = health
        self.profession = profession


GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
ENDG = "\033[0m"
ORANGE = "\033[38;5;214m"
LIGHT_GREEN = "\033[38;5;82m"
boollist = [0,0,0,0,0,0,0,0]
professions = ["лікарем","вчителем","інженером","програмістом","архітектором","юристом","дизайнером","журналістом",
    "електриком","психологом","пілотом","механіком","медсестрою","ветеринаром","офіціантом","барменом","кухарем",
    "фотографом","режисером","актором","співаком","музикантом","художником","скульптором","хіміком","біологом",
    "фізиком","геологом","астрономом","економістом","бухгалтером","маркетологом","соціологом","істориком","філологом",
    "політологом","дипломатом","пожежником","поліцейським","листоношею","тренером","спортсменом",
    "агентом з нерухомості","перекладачем","адвокатом","секретарем","менеджером","аналітиком","логістом","водієм",
    "оператором кол-центру","будівельником","малярем","сантехніком","садівником","фермером","пекарем","логопедом",
    "інструктором з йоги","бортпровідником","оператором на виробництві","продавцем","бібліотекарем","лісником",
    "ландшафтним дизайнером","консультантом","інженером-будівельником","інженером-механіком","хореографом","модельєром",
    "спеціалістом з PR","мікробіологом","фінансовим аналітиком","сценаристом","ілюстратором","гейм-дизайнером",
    "косметологом","стоматологом","лаборантом","офтальмологом","логістиком","інспектором","льотчиком-випробувачем",
    "ріелтором","програмістом-розробником","системним адміністратором","спеціалістом із захисту інформації",
    "картографом","моряком","диспетчером","агрономом","вихователем","швеєю","стилістом","антикваром","археологом",
    "ентомологом","промоутером","оцінювачем","аналітиком даних"]
names = ["Олексій", "Ірина", "Дмитро", "Катерина", "Владислав", "Марина", "Сергій", "Оксана", "Максим", "Анастасія",
         "Юрій", "Тетяна", "Артем", "Вікторія", "Володимир", "Ольга", "Євген", "Наталія", "Павло", "Алла", "Анна",
         "Влад", "Михайло"]
part1 = ["Не зупиняйся,","Ти на правильному шляху,","Продовжуй рухатися вперед,","Кожен день ти стаєш кращим,",
         "Твої зусилля не марні,","Ти сильніший, ніж думаєш,","З кожним кроком ти ближче до мети,",
         "Твоя праця приносить плоди,","Кожен новий день — новий шанс,","Не здавайся,","Працюй над собою,",
         "Ти здатний на більше,","Сьогодні — час для дій,","Продовжуй боротися,",
         "Кожна маленька перемога має значення,","Ти можеш подолати будь-які труднощі,","Кожен крок — це успіх,",
         "Не бійся йти вперед,","Вір у свої сили,","Кожен новий виклик робить тебе сильнішим,"]
part2 = ["ти вже близько до своєї цілі!","успіх чекає на тебе!","зміни починаються з маленьких кроків.",
         "ти сильніший, ніж вчора.","кожен зусилля робить тебе ближче до мети.","ти робиш неймовірне!",
         "зміни відбуваються, навіть якщо ти їх не бачиш.","успіх — це результат постійних зусиль.",
         "продовжуй діяти, і ти побачиш результат.","ти створюєш своє майбутнє зараз.",
         "з кожним днем ти стаєш на крок ближче до мрії.","ти здатен досягти всього, що захочеш.",
         "кожне випробування робить тебе сильнішим.","все, що тобі потрібно — це вірити в себе.",
         "мрія стане реальністю завдяки твоїм зусиллям.","завдяки твоїй наполегливості, успіх неминучий.",
         "кожен твій крок — це вклад у майбутнє.","успіх приходить до тих, хто не зупиняється.",
         "кожен день ти на крок ближче до перемоги.","все можливо, якщо ти продовжуєш йти вперед."]
def motivation():
    print(f"'{BLUE}<{random.choice(part1)} {random.choice(part2)}>{ENDG}")
def water_intake(weight):
    water_needed = weight * 30
    print(f"\n{BLUE}<Вам потрібно випити {GREEN}{water_needed}{BLUE} мл води на день.>{ENDG}")
def imt(weight, height):
    bmi = weight / ((height / 100) ** 2)
    if bmi < 18.5:
        category = f"{YELLOW}<Недостатня вага>{ENDG}"
    elif 18.5 <= bmi < 24.9:
        category = f"{GREEN}<Норма>{ENDG}"
    elif 25 <= bmi < 29.9:
        category = f"{YELLOW}<Надмірна вага>{ENDG}"
    else:
        category = f"{RED}<Ожиріння>{ENDG}"
    print(category)
def heart_rate_zones(age):
    max_heart_rate = 220 - age
    print(f"{BLUE}Максимальна частота серцевих скорочень: {GREEN}{max_heart_rate}{BLUE} уд/хв")
    print(
        f"Зона спокою (50-60%): {GREEN}{round(max_heart_rate * 0.50, 2)} - {round(max_heart_rate * 0.60, 2)}{BLUE} уд/хв")
    print(
        f"Зона жироспалювання (60-70%): {GREEN}{round(max_heart_rate * 0.60, 2)} - {round(max_heart_rate * 0.70, 2)}{BLUE} уд/хв")
    print(
        f"Аеробна зона (80-90%): {GREEN}{round(max_heart_rate * 0.80, 2)} - {round(max_heart_rate * 0.90, 2)}{BLUE} уд/хв")
    print(
        f"Анаеробна зона (90-95%): {GREEN}{round(max_heart_rate * 0.90, 2)} - {round(max_heart_rate * 0.95, 2)}{BLUE} уд/хв")
    print(
        f"Червона зона (95-100%): {GREEN}{round(max_heart_rate * 0.95, 2)} - {round(max_heart_rate * 1.00, 2)}{BLUE} уд/хв{ENDG}")
def calories(weight, activity, duration):
    activity_data = {"біг": 0.063,
                     "плавання": 0.050,
                     "їзда на  велосипеді": 0.045,
                     "йога": 0.034,
                     "ходьба": 0.035,
                     "тренажери": 0.055}
    if activity not in activity_data:
        print(f"{RED}{activity} немає в списку можливих активностей{ENDG}")
    else:
        print(f"{BLUE}Ви спалили {GREEN}{round(weight * activity_data[activity] * duration, 2)}{BLUE} за"
              f" {GREEN}{duration}{BLUE} хвилин{ENDG}")
def sleep_calculator(age):
    if age <= 2:
        recommended_sleep = f"{GREEN}11-14 годин{ENDG}"
    elif 3 <= age <= 5:
        recommended_sleep = f"{GREEN}10-13 годин{ENDG}"
    elif 6 <= age <= 12:
        recommended_sleep = f"{YELLOW}9-12 годин{ENDG}"
    elif 13 <= age <= 17:
        recommended_sleep = f"{YELLOW}8-10 годин{ENDG}"
    elif 18 <= age <= 64:
        recommended_sleep = f"{RED}7-9 годин{ENDG}"
    else:
        recommended_sleep = f"{RED}7-8 годин{ENDG}"
    print(f"{BLUE}Рекомендована тривалість сну для вашого віку ({age}): {recommended_sleep}{ENDG}")

while True:
    print(f"{LIGHT_GREEN}<МЕНЮ ДЛЯ ТРЕНЕРА>\n"
          f"<{BLUE}1.{ORANGE if bool(boollist[0]) else LIGHT_GREEN} Потрібна мотивація?🤔{RED}(Різноманітні відповіді!){LIGHT_GREEN}>\n"
          f"<{BLUE}2.{ORANGE if bool(boollist[1]) else LIGHT_GREEN} Калькулятор ІМТ🍴{LIGHT_GREEN}>\n"
          f"<{BLUE}3.{ORANGE if bool(boollist[2]) else LIGHT_GREEN} Калькулятор обʼєму води на вагу💧{LIGHT_GREEN}>\n"
          f"<{BLUE}4.{ORANGE if bool(boollist[3]) else LIGHT_GREEN} Калькулятор ЧСС❤️{LIGHT_GREEN}>\n"
          f"<{BLUE}5.{ORANGE if bool(boollist[4]) else LIGHT_GREEN} Калькулятор спалення калорій🏃️{LIGHT_GREEN}>\n"
          f"<{BLUE}6.{ORANGE if bool(boollist[5]) else LIGHT_GREEN} Знайти клієнта🧑‍💻{RED}(Різноманітні відповіді!){LIGHT_GREEN}>\n"
          f"<{BLUE}7.{ORANGE if bool(boollist[6]) else LIGHT_GREEN} Калькулятор сну💤{LIGHT_GREEN}>\n"
          f"<{BLUE}8.{ORANGE if bool(boollist[7]) else LIGHT_GREEN} Про програму🤖{LIGHT_GREEN}>\n"
          f"<{BLUE}0.{LIGHT_GREEN} Вихід❌️>{ENDG}")
    choice = int(input(f"{LIGHT_GREEN}Оберіть функцію з меню >>{ENDG}"))
    if choice == 0:
        print(f"{BLUE}<Допобачення! Дякую, що скористувались послугами програми!👋>{ENDG}")
        exit()
    elif choice == 1:
        boollist[0]=1
        motivation()
        input(f"{LIGHT_GREEN}Щоб продовжити, натисніть Enter{ENDG}")
    elif choice == 2:
        boollist[1]=1
        imt(float(input("Введіть вашу вагу>>")), float(input("Введість ваш зріст>>")))
        input(f"{LIGHT_GREEN}Щоб продовжити, натисніть Enter{ENDG}")
    elif choice == 3:
        boollist[2]=1
        water_intake(float(input("Введіть вашу вагу>>")))
        input(f"{LIGHT_GREEN}Щоб продовжити, натисніть Enter{ENDG}")
    elif choice == 4:
        boollist[3]=1
        heart_rate_zones(int(input("Введіть ваш вік>>")))
        input(f"{LIGHT_GREEN}Щоб продовжити, натисніть Enter{ENDG}")
    elif choice == 5:
        boollist[4]=1
        calories(float(input("Введіть вашу вагу>>")),
                 input(f"{GREEN}Можливі активності: \nбіг, плавання, їзда на велосипеді,йога, ходьба, тренажери{ENDG}\nВведіть активність>>"),
                 float(input("Введіть час виконання вправи (в хвилинах) >>")))
        input(f"{LIGHT_GREEN}Щоб продовжити, натисніть Enter{ENDG}")
    elif choice == 6:
        boollist[5]=1
        age = random.randint(25, 70)
        client = Client(random.choice(names), age, random.randint(3000, 50000),
                        random.randint(0, 40) if age > 60 else random.randint(0, 13),
                        random.choice(["здорова", "слабка", "повільна", "товста", "худа"]), random.choice(professions))
        if 11 <= client.experience < 21:
            rokiv = "років"
        else:
            if str(client.experience)[-1] == "1":
                rokiv = "рік"
            elif 2 <= int(str(client.experience)[-1]) < 5:
                rokiv = "роки"
            else:
                rokiv = "років"
        if str(client.age)[-1] == "1":
            rokiv2 = "рік"
        elif 2 <= int(str(client.age)[-1]) < 5:
            rokiv2 = "роки"
        else:
            rokiv2 = "років"
        print(f"{client.name}, {client.health} людина,"
              f" {client.age} {rokiv2}. Зарплатня: {client.price} і працює "
              f"{'аж ' + str(client.experience) if client.experience > 10 else client.experience} "
              f"{rokiv} {client.profession}")
        input(f"{LIGHT_GREEN}Щоб продовжити, натисніть Enter{ENDG}")
    elif choice == 7:
        boollist[6]=1
        sleep_calculator(int(input("Введіть ваш вік>>")))
        input(f"{LIGHT_GREEN}Щоб продовжити, натисніть Enter{ENDG}")
    elif choice == 8:
        boollist[7]=1
        print(
            f"{BLUE}<Програма написана для творчого завдання з Основ програмування студентом Ковальчук Адам 122 1 курс.🎓📘\n"
            f"Всі збіги, крім імені студента, який виконував роботу, випадкові!😄✨\n"
            f"Гарного Вам дня!☀️😊🍄\n"
            f"Можливо невідомві абривіатури:\n"
            f"ІМТ - індекс маси тіла\n"
            f"ЧСС - частота скорочення серця>{ENDG}")
        input(f"{LIGHT_GREEN}Щоб продовжити, натисніть Enter{ENDG}")
    else:
        print(f"{RED}ПУНКТ НЕ ІСНУЄ!{ENDG}")
        input(f"{LIGHT_GREEN}Щоб продовжити, натисніть Enter{ENDG}")
