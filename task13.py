#13
import math
def calculate_area(radius1, radius2):
    inner_radius = min(radius1, radius2)
    outer_radius = max(radius1, radius2)
    area1 = math.pi * inner_radius * inner_radius
    area2 = math.pi * outer_radius * outer_radius
    area = area2 - area1
    return area

radius1 = float(input("Введите первый радиус: "))
radius2 = float(input("Введите второй радиус: "))

coverage_area = calculate_area(radius1, radius2)
print(f"Площадь покрываемой территории: {coverage_area} квадратных единиц")