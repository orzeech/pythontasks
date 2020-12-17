import re


def get_id(id):
    with open('DataBase.txt', 'r', encoding='utf-8') as line_by_line:
        ID_as_string = str(id)
        try:
            for line in line_by_line:
                table = line.split(':')
                if table[0] == ID_as_string:
                    return line
        finally:
            line_by_line.close()


def find(word):
    with open('DataBase.txt', 'r', encoding='utf-8') as line_by_line2:
        try:
            result = []
            for line in line_by_line2:
                table = re.split(':|, | |! ', line)
                table2 = line.split(':')
                for i in range(len(table)):
                    if table[i][-1] == '.' or table[i][-1] == '?':
                        table[i] = table[i][:-1]
                for i in range(len(table)):
                    if word.lower() == table[i].lower() or word.lower() + '.\n' == table[i].lower()\
                            or word.lower() + '!\n' == table[i].lower() or word.lower() + '?\n' == table[i].lower():
                        result += table2[1:]
            return result
        finally:
            line_by_line2.close()


if __name__ == '__main__':
    print(get_id(2))
    print(''.join(find("Wredny")))