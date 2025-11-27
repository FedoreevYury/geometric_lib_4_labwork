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
3. ee6e8add7b16a3a927342f0448f5cdf747be45b3 добавлен комментарий в файл circle.py
4. 04ad4226ea833f42ebb7f3379950f5a2fba3b870 добавлен комментарий в файл square.py
5. f40337791313cf57dc16be0458f5843bd8b19d17 добавлены файлы triangle.py и rectangle.py
