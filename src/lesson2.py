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


def read_line_by_line(filename):
    with open(filename, 'r', encoding='utf-8') as line_by_line_stream:
        for line in line_by_line_stream:
            print(line)


if __name__ == '__main__':
    print(read_content_from_file('../whatever.txt'))
    read_line_by_line('../whatever.txt')
