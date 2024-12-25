import sys

def read_circle_data(filename):
    with open(filename, 'r') as file:
        center_x, center_y = map(float, file.readline().strip().split())
        radius = float(file.readline().strip())
    return (center_x, center_y), radius

def read_points_data(filename):
    with open(filename, 'r') as file:
        points = [tuple(map(float, line.strip().split())) for line in file]
    return points

def position_relative_to_circle(circle_center, radius, point):
    dx = point[0] - circle_center[0]
    dy = point[1] - circle_center[1]
    distance_squared = dx * dx + dy * dy
    radius_squared = radius * radius
    
    if distance_squared < radius_squared:
        return 1  # Точка внутри окружности
    elif distance_squared == radius_squared:
        return 0  # Точка на окружности
    else:
        return 2  # Точка снаружи окружности

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: KarpychevAlexandrPython.txt circle.txt points.txt")
        sys.exit(1)

    circle.txt = sys.argv[1]
    points.txt = sys.argv[2]

    # Чтение данных из файлов
    circle.txt, radius = read_circle_data(circle.txt)
    points.txt = read_points_data(points.txt)

    # Определение положения каждой точки относительно окружности
    results = [position_relative_to_circle(circle_center, radius, point) for point in points]

    # Вывод результатов
    for result in results:
        print(result)
