# Рекурсивная функция для чтения строк файла
def read_lines(file, lines=None):
    if lines is None:
        lines = []
    line = file.readline()
    if not line:
        return lines
    return read_lines(file, lines + [line.rstrip('\n')])

# Рекурсивная функция для удаления дубликатов
def unique(lst, seen=None):
    if seen is None:
        seen = set()
    if not lst:
        return []
    first, rest = lst[0], lst[1:]
    if first in seen:
        return unique(rest, seen)
    return [first] + unique(rest, seen | {first})

# Рекурсивная функция для разбора строки CSV
def parse_line(line, delimiter='|', result=None):
    if result is None:
        result = []
    if not line:
        return result
    if delimiter not in line:
        return result + [line]
    pos = line.index(delimiter)
    return parse_line(line[pos+1:], delimiter, result + [line[:pos]])

# Рекурсивная функция для конвертации типов
def convert_types(book):
    if not book:
        return []
    return [book[0], book[1], book[2], int(book[3]), float(book[4])]

# Рекурсивная функция для применения map к списку
def map_list(func, lst, index=0, result=None):
    if result is None:
        result = []
    if index >= len(lst):
        return result
    return map_list(func, lst, index + 1, result + [func(lst[index])])

# Задание 1: получить список книг из файла
def get_books(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = read_lines(f)
    
    # Убираем дубликаты и пропускаем заголовок
    unique_lines = unique(lines)[1:]
    
    # Парсим строки
    parsed = map_list(parse_line, unique_lines)
    
    # Конвертируем типы
    converted = map_list(convert_types, parsed)
    
    return converted

# Рекурсивная функция для фильтрации
def filter_list(predicate, lst, index=0, result=None):
    if result is None:
        result = []
    if index >= len(lst):
        return result
    if predicate(lst[index]):
        return filter_list(predicate, lst, index + 1, result + [lst[index]])
    return filter_list(predicate, lst, index + 1, result)

# Рекурсивная функция для объединения title и author 
def merge_title_author(book):
    # После объединения: [isbn, "title, author", quantity, price]
    return [book[0], f"{book[1]}, {book[2]}", book[3], book[4]]

# Задание 2: фильтрация книг по подстроке
def filtered_books(books, substring):
    # Фильтруем книги по названию (book[1])
    filtered = filter_list(
        lambda book: substring.lower() in book[1].lower(),
        books
    )
    # Объединяем title и author
    merged = map_list(merge_title_author, filtered)
    return merged

# Рекурсивная функция для создания кортежей с общей стоимостью
def make_cost_tuple(book):
    # book[0] - isbn, book[2] - quantity, book[3] - price
    return (book[0], book[2] * book[3])

# Задание 3: подсчет общей стоимости
def total_cost(filtered_books):
    return map_list(make_cost_tuple, filtered_books)

# Пример использования
if __name__ == "__main__":
    books = get_books("books.csv")
    print("Все книги:")
    print(books)
    print(f"Всего книг: {len(books)}")
    
    python_books = filtered_books(books, "python")
    print("Книги с 'python' в названии:")
    print(python_books)
    print(f"Найдено книг: {len(python_books)}")
    
    costs = total_cost(python_books)
    print("Общая стоимость (isbn, total):")
    print(costs)