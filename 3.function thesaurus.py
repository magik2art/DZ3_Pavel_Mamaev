glossary_num = {
    "И": tuple(["Иван", "Илья"]),
    "М": tuple(["Мария", "Маруся"]),
    "П": tuple(["Петр", "Павел"]),
    "Н": tuple(["Николай", "Наталья"])
    }

book_of_workers = []

def thesaurus(first_symbol):
    i = 0
    global book_of_workers
    array = []
    while i < len(first_symbol):
        array.append(glossary_num.get(first_symbol[i]))
        i += 1
        print(array)
    book_of_workers = array
    print(book_of_workers)
    return book_of_workers



first_charaster = input("Введите имена сотрудников через запятую(Например: Игорь, Иван): ")
print(first_charaster)
first_charaster = first_charaster.upper()
print(first_charaster)
first_charaster = first_charaster.split(", ")
print(first_charaster)

i = 0
first_symbol = []
while i < len(first_charaster):
    first_symbol.append(first_charaster[i][0])
    i += 1

first_symbol = list(set(first_symbol))
print(first_symbol)
thesaurus(first_symbol)
print(book_of_workers)
