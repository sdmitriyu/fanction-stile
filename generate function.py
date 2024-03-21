# Фабрика функций
def create_operation(operator):
    if operator == "multiply":
        def multiply(x, y):
            return x * y

        return multiply
    elif operator == "divide":
        def divide(x, y):
            if y != 0:
                return x / y
            else:
                return "Error: Division by zero"

        return divide


my_func_multiply = create_operation("multiply")
my_func_divide = create_operation("divide")

print(my_func_multiply(4, 2))
print(my_func_divide(4, 2))

# Лямбда-Функции
multiply = lambda x: x ** 2

def multiply_def(x):
    return x ** 2

print(multiply(4))
print(multiply_def(4))


# Вызываемые Объекты
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


rectangle = Rect(2, 4)
print("Стороны: {}, {}".format(rectangle.a, rectangle.b))
print("Площадь: {}".format(rectangle()))
