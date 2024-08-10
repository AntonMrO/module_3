call = 0
def count_call():
    global call
    call += 1

def string_info(string):
    count_call()
    string = (len(string), string.upper(), string.lower())
    return string

def is_contains(string, list_to_search):
    count_call()
    for i in range(len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            str_count = True
            break
        else: str_count = False
    return str_count



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(call)