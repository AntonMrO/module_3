# Задача "Рекурсивное умножение цифр"
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    # print(str_number, first)
    if len(str_number) > 1 and int(str_number[1:]) != 0: #multiply by zero gives zero, excluding zero at the end of a list
        return first * get_multiplied_digits(int(str_number[1:]))   #recursion
    else:
        return first

result = get_multiplied_digits(40203)
print(result)

result = get_multiplied_digits(20000222222000)   #two to the 7th power, the zeros at the end are not taken
print(result)