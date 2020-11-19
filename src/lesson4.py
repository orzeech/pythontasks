def log(f, arg):
    print("I'm doing something with " + str(arg) + " TBH I don't know what I'm doing")
    print(f(arg))

def validator(validate_function, arg):
    print("Validating " + str(arg))
    return validate_function(arg-60)

# my_function and this one are in reality the same
def adder(a, b):
    return a + b

if __name__ == '__main__':
    my_function = lambda a, b: a + b
    my_doubler = lambda x: 2*x
    sum_checker = lambda a, b, c: a + b == c
    print(my_function(7, 3))
    print(my_doubler(10))
    print(sum_checker(4, 5, 9))
    print(sum_checker(4, 5, 7))
    log(my_doubler, 55)

    # Liczby maja byc wieksze od 10 i podzielne przez 2
    is_divided_by_two = lambda x: x % 2 == 0
    is_greater_than_ten = lambda whatev: whatev > 10
    liczba = 66
    print(validator(is_divided_by_two, liczba))
    print(validator(is_greater_than_ten, liczba))