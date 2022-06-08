def is_perfect(number):
    number_list = [i for i in range(1, number) if number % i == 0]
    if number_list:
        return number_list
    else:
        return False


