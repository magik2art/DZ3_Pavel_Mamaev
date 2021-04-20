def num_translate(Numbers):
    glossary = [
        ['one', 'один', 1],
        ['two', 'два', 2],
        ['three', 'три', 3],
        ['four', 'четыре', 4],
        ['five', 'пять', 5],
        ['six', 'шесть', 6],
        ['seven', 'семь', 7],
        ['eight', 'восемь', 8],
        ['nine', 'девять', 9],
        ['ten', 'десять', 10],
    ]

    i = 0
    while i < len(glossary):
        if input_number == glossary[i][0]:
            return glossary[i][1]
        elif input_number == glossary[i][1]:
            return glossary[i][0]
        elif input_number == glossary[i][2]:
            return glossary[i][1]
    return print(None)


Numbers = input("Введите число от 0 до 10 ")
num_translate(Numbers)

