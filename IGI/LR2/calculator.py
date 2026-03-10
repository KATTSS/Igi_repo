import os
from geometric_lib.circle import area as circle_area, perimeter as circle_perimeter
from geometric_lib.square import area as square_area, perimeter as square_perimeter

figure = os.getenv('FIGURE', 'square') 
side_a = float(os.getenv('SIDE_A', 5))
side_b = os.getenv('SIDE_B') 

print(f"Выполняем вычисления для фигуры: {figure}")

if figure == 'circle':
    radius = side_a
    print(f"Радиус круга: {radius}")
    print(f"Площадь круга: {circle_area(radius)}")
    print(f"Периметр круга (длина окружности): {circle_perimeter(radius)}")

elif figure == 'square':
    side = side_a
    print(f"Сторона квадрата: {side}")
    print(f"Площадь квадрата: {square_area(side)}")
    print(f"Периметр квадрата: {square_perimeter(side)}")

elif figure == 'rectangle':
    if side_b is None:
        print("Ошибка: Для прямоугольника нужно задать SIDE_B")
    else:
        side_b = float(side_b)
        print(f"Стороны прямоугольника: {side_a} и {side_b}")
        area = side_a * side_b
        perimeter = 2 * (side_a + side_b)
        print(f"Площадь прямоугольника: {area}")
        print(f"Периметр прямоугольника: {perimeter}")
else:
    print(f"Неизвестная фигура: {figure}. Допустимо: circle, square, rectangle")