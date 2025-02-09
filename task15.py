#15
cm = float(input("Введите расстояние в сантиметрах: "))
inches = cm / 2.54
feet = inches / 12
yards = feet / 3
miles = yards / 1760

print(f"Ярды: {yards}")
print(f"Мили: {miles}")
print(f"Футы: {feet}")
print(f"Дюймы: {inches}")