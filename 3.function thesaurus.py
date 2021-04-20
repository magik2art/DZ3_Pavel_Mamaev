glossary_num = {
    "и": tuple(["иван", "илья"]),
    "м": tuple(["мария", "маруся"]),
    "п": tuple(["петр", "павел"]),
    "н": tuple(["николай", "наталья"])
    }

book_of_workers = []

def thesaurus(first_symbol):
    i = 0
    array = []
    while i < len(first_symbol):
        array.append(glossary_num.get(first_symbol[i]))
        i += 1
    book_of_workers = array
    print(book_of_workers)

first_charaster = input("Введите имена сотрудников через запятую(Например: Игорь, Иван): ")
first_charaster = first_charaster.lower()
first_charaster = first_charaster.split(", ")

i = 0
first_symbol = []
while i < len(first_charaster):
    first_symbol.append(first_charaster[i][0])
    i += 1

first_symbol = list(set(first_symbol))

thesaurus(first_symbol)
