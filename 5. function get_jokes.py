import random

def get_jokes(num_jokes):
    i = 0
    sum_jokes = []
    while i < num_jokes:
        random.choice(random_massiv[0]), random.choice(random_massiv[1]), random.choice(random_massiv[2])
        jokes = [[[random.choice(random_massiv[0])], [random.choice(random_massiv[1])], [random.choice(random_massiv[2])]]]
        sum_jokes.append("".join(str(jokes)))
        i += 1

    print("Итог = ", sum_jokes)

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# чтобы было интереснее я решил сделать рандомный выбор 1, 2 и 3 массивов
massiv = [nouns] + [adverbs] + [adjectives] # делаем массив для того чтобы выбирать 1 из них рандомом
i = 0
r = 2 # количество массивов для перебора
random_massiv = []
while i < 3:
    random_massiv.append(massiv.pop(random.randint(0, r))) # делаем рандон массива для 1, 2 и 3 слова в будующем
    r -= 1
    i += 1

jokes = int(input("Введите количество необходимых для генерации шуток: "))

get_jokes(jokes)
