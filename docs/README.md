# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# descriphion of def
## circle.py
### def area (r)
- функция принимает r - радиус круга;
- функция возвращяет:  math.pi - число пи (3,14159...) умноженное на r*r
- в итоге получаем площадь круга

- Пример r = 5; print(ares(r)) = 78.53981633974483 - площадь круга

### def perimeter(r)
- функция принимает r - радиус круг; 
- функция возвращает:  math.pi - число пи(3,14159...) умноженное на 2 и на r - радиус круга
- в итоге получаем длину окружности

- Пример: r = 5; print(perimeter(r)) = 31.41592653589793 - длинна окружности

## square.py
### def area(a)
- функция принимает число а, возвращает квадрат числа a
- Пример: a = 2; print(area(a)) = 4 - площадь квадрата

### def perimeter(a)
- функция принимает число a, возвращает 4 * а - периметр квадрата
- Пример: a = 2; print(perimeter(a)) = 8 - периметр квадрата

## rectangle.py
### def area (a, b)
- эта функция принимает int a и int b - целые числа, возвращает a * b - площадь прямоугольника
- Пример: a = 2, b = 3; print(area(a, b)) = 6 - площадь прямоугольника

### def perimeter
- функция принимает int a и int b - целые числа, возвращает 2 * (a + b) - периметр прямоугольника
- Пример: a = 2, b = 3; print(perimeter(a, b)) = 10 периметр прямоугольника

## triangle.py
### def area
- функция принимает int a и int h - целые числа, возвращает a * h / 2 - площадь треугольника
- Пример: a = 2, h = 3; print(area(a, h)) = 3 - площадь треугольника

### def perimeter
- функция принимает int a, int b и int c - целые числа, возвращает a + b + c - периметр треугольника
- Пример: a = 2, b = 3, c = 4; print(perimeter(a, b, c)) = 9 - периметр треугольника

# project change history
1. 8ba9aeb3cea847b63a91ac378a2a6db758682460 добавленны файлы circle.py и square.py
2. d078c8d9ee6155f3cb0e577d28d337b791de28e2 добавлен файл Docs
3. fef5149e3096fd77d2a895215bc06062238a6a0a добавлен комментарий в файл circle.py
4. 35609bf5595e0323aab1c76a1f69c933f174c9c9 добавлен комментарий в файл square.py
5. cf20ef838235bcaa322e1c6f2f6537e177b34c09 добавлены файлы triangle.py и rectangle.py
6. 83581ee328e5eecfe9150ef4983132a19351a908 added __unit__.py
7. 842698e930d3972122c14f8b4f6cca67fae07b8c added tests_triangle.py
8. 9bced8534c80de74235646b305aad7151849dbb2 fixed tests_triangle.py
9. 4d605b7e5e8920fc274cb15486a37cebc0a02780 added tests_circle.py
10. 633e389e5c791bef044f2484d3ce06d8bb008b4a added tests_square.py
