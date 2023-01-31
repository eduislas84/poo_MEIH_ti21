def area_del_triangulo(a, b, c):
    # Perímetro
    p = a + b + c

    # Semi-perímetro
    s = p / 2

    # Area por Herón
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    return area, p

area, perimeter = area_del_triangulo(3, 4, 5)
print("El área es:", area)
print("El perímetro es:", perimeter)