def read_data(file_name):
    with open(file_name, encoding='utf-8', newline='') as f:
        data_reader = csv.reader(f, delimiter='|')
        next(data_reader)
        return list(map(
            lambda rec: [rec[0], rec[1], rec[2], int(rec[3]), float(rec[4])],
            data_reader
        ))

def filter_by_author(collection, fragment):
    fragment_lower = fragment.lower()
    return list(map(
        lambda item: [item[0], f'{item[1]}, {item[2]}', item[3], item[4]],
        filter(lambda item: fragment_lower in item[1].lower(), collection)
    ))

def multiply_fields(entries):
    return list(map(
        lambda entry: (entry[0], entry[2] * entry[3]),
        entries
    ))

if __name__ == '__main__':
    library = read_data("books.csv")
    print("задание 1:")
    print(library)

    filtered = filter_by_author(library, "python")
    print("задание 2:")
    print(filtered)

    result = multiply_fields(filtered)
    print("задание 3:")
    print(result)
