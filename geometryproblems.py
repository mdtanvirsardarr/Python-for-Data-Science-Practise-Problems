# 1. Check the leap year or not
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "It is a leap year"
    else:
        return "It is not a leap year"

n = int(input("Enter a year to check if it is a leap year or not: "))
print(is_leap_year(n))


# 2. Area of a circle
def area_of_circle(radius):
    area = 3.1415 * radius * radius
    return area

radius = float(input("Enter the radius of the circle: "))
print("Area of the circle is", area_of_circle(radius))


# 3. Circumference of a circle
def circumference_of_circle(radius):
    circumference = 2 * 3.1415 * radius
    return circumference

radius = float(input("Enter the radius of the circle: "))
print("Circumference of the circle is", circumference_of_circle(radius))


# 4. Area of a rectangle
def area_of_rectangle(length, width):
    area = length * width
    return area

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print("Area of the rectangle is", area_of_rectangle(length, width))


# 5. Perimeter of a rectangle
def perimeter_of_rectangle(length, width):
    perimeter = 2 * (length + width)
    return perimeter

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print("Perimeter of the rectangle is", perimeter_of_rectangle(length, width))


# 6. Area of a square
def area_of_square(side):
    area = side * side
    return area

side = float(input("Enter the side of the square: "))
print("Area of the square is", area_of_square(side))


# 7. Perimeter of a square
def perimeter_of_square(side):
    perimeter = 4 * side
    return perimeter

side = float(input("Enter the side of the square: "))
print("Perimeter of the square is", perimeter_of_square(side))


# 8. Area of a triangle
def area_of_triangle(base, height):
    area = 0.5 * base * height
    return area

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
print("Area of the triangle is", area_of_triangle(base, height))


# 9. Perimeter of a triangle
def perimeter_of_triangle(a, b, c):
    perimeter = a + b + c
    return perimeter

a = float(input("Enter first side of the triangle: "))
b = float(input("Enter second side of the triangle: "))
c = float(input("Enter third side of the triangle: "))
print("Perimeter of the triangle is", perimeter_of_triangle(a, b, c))


# 10. Area of a parallelogram
def area_of_parallelogram(base, height):
    area = base * height
    return area

base = float(input("Enter the base of the parallelogram: "))
height = float(input("Enter the height of the parallelogram: "))
print("Area of the parallelogram is", area_of_parallelogram(base, height))


# 11. Area of a trapezium
def area_of_trapezium(a, b, height):
    area = 0.5 * (a + b) * height
    return area

a = float(input("Enter first parallel side of the trapezium: "))
b = float(input("Enter second parallel side of the trapezium: "))
height = float(input("Enter the height of the trapezium: "))
print("Area of the trapezium is", area_of_trapezium(a, b, height))


# 12. Area of a rhombus
def area_of_rhombus(d1, d2):
    area = 0.5 * d1 * d2
    return area

d1 = float(input("Enter first diagonal of the rhombus: "))
d2 = float(input("Enter second diagonal of the rhombus: "))
print("Area of the rhombus is", area_of_rhombus(d1, d2))


# 13. Surface area of a cube
def surface_area_of_cube(side):
    surface_area = 6 * side * side
    return surface_area

side = float(input("Enter the side of the cube: "))
print("Surface area of the cube is", surface_area_of_cube(side))


# 14. Volume of a cube
def volume_of_cube(side):
    volume = side * side * side
    return volume

side = float(input("Enter the side of the cube: "))
print("Volume of the cube is", volume_of_cube(side))


# 15. Surface area of a cuboid
def surface_area_of_cuboid(length, width, height):
    surface_area = 2 * (length * width + length * height + width * height)
    return surface_area

length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))
print("Surface area of the cuboid is", surface_area_of_cuboid(length, width, height))


# 16. Volume of a cuboid
def volume_of_cuboid(length, width, height):
    volume = length * width * height
    return volume

length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))
print("Volume of the cuboid is", volume_of_cuboid(length, width, height))


# 17. Surface area of a cylinder
def surface_area_of_cylinder(radius, height):
    surface_area = 2 * 3.1415 * radius * (radius + height)
    return surface_area

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
print("Surface area of the cylinder is", surface_area_of_cylinder(radius, height))


# 18. Volume of a cylinder
def volume_of_cylinder(radius, height):
    volume = 3.1415 * radius * radius * height
    return volume

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
print("Volume of the cylinder is", volume_of_cylinder(radius, height))


# 19. Surface area of a sphere
def surface_area_of_sphere(radius):
    surface_area = 4 * 3.1415 * radius * radius
    return surface_area

radius = float(input("Enter the radius of the sphere: "))
print("Surface area of the sphere is", surface_area_of_sphere(radius))


# 20. Volume of a sphere
def volume_of_sphere(radius):
    volume = (4 / 3) * 3.1415 * radius * radius * radius
    return volume

radius = float(input("Enter the radius of the sphere: "))
print("Volume of the sphere is", volume_of_sphere(radius))


# 21. Diagonal of a rectangle
def diagonal_of_rectangle(length, width):
    diagonal = (length * length + width * width) ** 0.5
    return diagonal

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print("Diagonal of the rectangle is", diagonal_of_rectangle(length, width))


# 22. Hypotenuse of a right triangle
def hypotenuse_of_triangle(a, b):
    hypotenuse = (a * a + b * b) ** 0.5
    return hypotenuse

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
print("Hypotenuse is", hypotenuse_of_triangle(a, b))