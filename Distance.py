# Точечные объекты имеют атрибуты x и y.
# Напиcать функцию, вычисляющую расстояние между точкой a и точкой b.
import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
# AB = √(xb - xa)2 + (yb - ya)2
def distance(a,b):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

if __name__ == '__main__':
    x1, y1 = map(int, input("Enter the x and y coordinates of the first point separated by a space: ").split())
    x2, y2 = map(int, input("Enter the x and y coordinates of the second point separated by a space: ").split())
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    print("Distance: ",format(distance(p1, p2)))
