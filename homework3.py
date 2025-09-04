#1 задание
pet_type = input("Введите вид питомца: ")
pet_name = input("Введите кличку питомца: ")
pet_age = input("Введите возраст питомца: ")

print("Это {pet_type} по кличке \"{pet_name}\". Возраст: {pet_age} года(лет).")

#2 задание

print("Введите этапы развития человека по порядку:")

stages = []

n = 7

for i in range(1, n + 1):
    stag = input(f"Введите этап {i}: ")
    stages.append(etap)

print(*stages, sep='=>')