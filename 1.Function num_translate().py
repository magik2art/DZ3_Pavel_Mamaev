glossary = {
    1: "one", 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'
}


def func_translate(num_for_translate):
    if 0 < num_for_translate < 11:
        print(glossary[num_for_translate])
    else:
        print(None)


while True:
    num_for_translate = input("Введите число от 0 до 10: ")
    if num_for_translate.isdigit():
        num_for_translate = int(num_for_translate)
        func_translate(num_for_translate)
        break
    else:
        print("Ошибка! Вы ввели текст, а нужно число")
