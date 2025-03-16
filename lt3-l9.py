# Task 1
current_temperature: int = 21
city: str = "Kyiv"

temperature_result: str = f"У {city.capitalize()} зараз {current_temperature} градусів Цельсія"
print(temperature_result)

# Task 2
user_name: str = input("Enter your name: ")
user_age: int = int(input("Enter your age (int): "))
user_city: str = input("Type where you live: ")

bio_result: str = (f"Імʼя: {user_name.capitalize()} \n"
                   f"Вік: {user_age} \n"
                   f"Місце проживання: {user_city.capitalize()} ")
print(bio_result)

# Task 3
user_lenght_side: int = int(input("Enter length (int): "))
user_width_side: int = int(input("Enter width (int): "))

perimeter: int = 2 * (user_lenght_side + user_width_side)
square: int = user_lenght_side * user_width_side

result_calculation: str = (f"Довжина: {user_lenght_side} \n"
                           f"Ширина: {user_width_side} \n"
                           f"Периметр: {perimeter} \n"
                           f"Площа: {square}")

print(result_calculation)

# Task 4
pupil_name: str = input("Enter your name: ").capitalize()
pupil_surname: str = input("Enter your surname: ").upper()
pupil_day_birth: str = input("Enter your day and months of birth: ")
pupil_favorite_subject: str = input("Enter yout favorite subject: ").lower()

pupil_resume_result: str = (f"Pupil name: {pupil_name} \n"
                            f"Pupil surname: {pupil_surname} \n"
                            f"Pupil was born: {pupil_day_birth} \n"
                            f"Pupil favorite subject: {pupil_favorite_subject}")

print(pupil_resume_result)
