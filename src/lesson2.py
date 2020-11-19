def read_content_from_file(filename):
    stream = open(filename, 'r', encoding='utf-8')
    try:
        content = stream.read()
        print(content)
    # print(100/0)
    finally:
        print('closing the stream')
        stream.close()
    return content

def get_line(line):
    return lambda l: "Printing line " + line


def read_line_by_line(filename):
    with open(filename, 'r', encoding='utf-8') as stream:
        for line in stream:
            print(get_line(line))


def read_line_by_line2(filename):
    stream = open(filename, 'r', encoding='utf-8')
    try:
        for line in stream:
            print(line)
    finally:
        stream.close()


if __name__ == '__main__':
    # print(read_content_from_file('../whatever.txt'))
    read_line_by_line('../whatever.txt')
    # read_line_by_line2('../whatever.txt')
