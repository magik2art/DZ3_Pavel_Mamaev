glossary_num = {
    1: "one", 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 0:'zero'
}

glossary_str = {
    'один': 'one', 'два': 'two', 'три': 'three', 'четыре': 'four', 'пять': 'five',
    'шесть': 'six', 'семь': 'seven', 'восемь': 'eight', 'девять': 'nine', 'десять': 'ten', 'ноль': 'zero'
}

def func_translate(num_for_translate):
    if 0 < num_for_translate < 11:
        print(glossary_num[num_for_translate])
    else:
        print(None)

def func_str_capitalize(num_for_translate):
    num_for_translate = num_for_translate.lower()
    if num_for_translate in glossary_str:
        num_for_translate = glossary_str[num_for_translate]
        print(num_for_translate.capitalize())
    else:
        print(None)

def func_str_translate(num_for_translate):
    if num_for_translate in glossary_str:
        num_for_translate = glossary_str[num_for_translate]
        print(num_for_translate)
    else:
        print(None)

num_for_translate = input("Введите число от 0 до 10: ")
if num_for_translate.isdigit():
    num_for_translate = int(num_for_translate)
    func_translate(num_for_translate)
elif num_for_translate[0].isupper():
    func_str_capitalize(num_for_translate)
else:
    func_str_translate(num_for_translate)
