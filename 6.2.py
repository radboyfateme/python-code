def filter_positive_integers(func):
    def wrapper(numbers):
        filtered_numbers = [n for n in numbers if isinstance(n, int) and n >= 0]
        return func(filtered_numbers)
    return wrapper

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

@filter_positive_integers
def calculate_factorials(numbers):
    return [factorial(n) for n in numbers]

number_list = [4, 3, 8, 0, -3, -45, 2, 10, -16, 23, 9, 1, -6, 55, 3.4, 6, 11.5]
factorial_list = calculate_factorials(number_list)
factorial_list

