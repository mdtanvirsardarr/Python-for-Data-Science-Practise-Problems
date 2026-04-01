# 1. Derivative of x^2 at a point
def derivative_of_x_square(x):
    h = 0.0001
    derivative = ((x + h) ** 2 - x ** 2) / h
    return derivative

x = float(input("Enter the value of x: "))
print("Derivative of x^2 at", x, "is", derivative_of_x_square(x))


# 2. Derivative of x^3 at a point
def derivative_of_x_cube(x):
    h = 0.0001
    derivative = ((x + h) ** 3 - x ** 3) / h
    return derivative

x = float(input("Enter the value of x: "))
print("Derivative of x^3 at", x, "is", derivative_of_x_cube(x))


# 3. Derivative of 5x + 3 at a point
def derivative_of_linear(x):
    h = 0.0001
    derivative = (5 * (x + h) + 3 - (5 * x + 3)) / h
    return derivative

x = float(input("Enter the value of x: "))
print("Derivative of 5x + 3 at", x, "is", derivative_of_linear(x))


# 4. Definite integral of x from a to b
def integral_of_x(a, b):
    integral = (b ** 2 - a ** 2) / 2
    return integral

a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
print("Integral of x from", a, "to", b, "is", integral_of_x(a, b))


# 5. Definite integral of x^2 from a to b
def integral_of_x_square(a, b):
    integral = (b ** 3 - a ** 3) / 3
    return integral

a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
print("Integral of x^2 from", a, "to", b, "is", integral_of_x_square(a, b))


# 6. Definite integral of x^3 from a to b
def integral_of_x_cube(a, b):
    integral = (b ** 4 - a ** 4) / 4
    return integral

a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
print("Integral of x^3 from", a, "to", b, "is", integral_of_x_cube(a, b))


# 7. Area under y = 2 from a to b
def integral_of_constant(a, b):
    integral = 2 * (b - a)
    return integral

a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
print("Integral of 2 from", a, "to", b, "is", integral_of_constant(a, b))


# 8. Slope of tangent to x^2 at a point
def slope_of_tangent_x_square(x):
    h = 0.0001
    slope = ((x + h) ** 2 - x ** 2) / h
    return slope

x = float(input("Enter the value of x: "))
print("Slope of tangent of x^2 at", x, "is", slope_of_tangent_x_square(x))


# 9. Equation of tangent to x^2 at a point
def tangent_line_x_square(x):
    y = x ** 2
    slope = 2 * x
    c = y - slope * x
    return slope, c

x = float(input("Enter the value of x: "))
m, c = tangent_line_x_square(x)
print("Equation of tangent is y =", m, "x +", c)


# 10. Area under y = x using trapezium rule
def trapezium_rule_for_x(a, b, n):
    h = (b - a) / n
    total = a + b

    for i in range(1, n):
        x = a + i * h
        total = total + 2 * x

    area = (h / 2) * total
    return area

a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
n = int(input("Enter number of intervals: "))
print("Approximate integral of x is", trapezium_rule_for_x(a, b, n))


# 11. Area under y = x^2 using trapezium rule
def trapezium_rule_for_x_square(a, b, n):
    h = (b - a) / n
    total = a ** 2 + b ** 2

    for i in range(1, n):
        x = a + i * h
        total = total + 2 * (x ** 2)

    area = (h / 2) * total
    return area

a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
n = int(input("Enter number of intervals: "))
print("Approximate integral of x^2 is", trapezium_rule_for_x_square(a, b, n))


# 12. Second derivative of x^2 at a point
def second_derivative_of_x_square(x):
    h = 0.0001
    second_derivative = ((x + h) ** 2 - 2 * (x ** 2) + (x - h) ** 2) / (h ** 2)
    return second_derivative

x = float(input("Enter the value of x: "))
print("Second derivative of x^2 at", x, "is", second_derivative_of_x_square(x))