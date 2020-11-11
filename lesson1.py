def print_hi(name):
    print('argument is ', name)
    return ' '.join(['Hello', name, name, name, name])


def list_operations():
    my_list = ['a', 'b', 'c']
    my_list.append('cokolwiek')
    length = len(my_list)
    print(length)

    for s in my_list:
        print(s)
        for i in range(50):
            print(i, s)
    for i, my_string in enumerate(my_list):
        print(i, my_string)
    for i in range(10):
        print(i)
    print_hi(my_list)


def maps_etc():
    global my_map
    my_list = ['raz', 'dwa', 'trzy']
    s = ', '.join(my_list)
    print(s)
    s.split()
    my_map = {
        'klucz': 'cokolwiek',
        'drugi_klucz': 56,
        'trzeci_klucz': 213
    }
    print(my_map['klucz'], my_map['drugi_klucz'])
    for key, value in my_map.items():
        print(key, value)
    # in = contains()
    print('raz' in my_list)
    print('raz' in my_map)


if __name__ == '__main__':
    s = print_hi('cokolwiek')
    print(s)

