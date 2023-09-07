'''
7.1[34]: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько 
слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху)
Если ритм есть, функция возвращает True, иначе возвращает False

Примеры/Тесты:
    <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
    <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
    <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
    <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
    <function_name>("Пам-парам-пурум Пум-пурум-карам") -> True
Примечание.

Подумайте об эффективности алгоритма. Какие структуры данных будут более эффективны по скорости.
Алгоритм должен работать так, чтобы не делать лишних проверок. Подумайте, возможно некоторые проверки не нужны.
(*) Усложнение.

Функция имеет параметр, который определяет, надо ли возвращать полную информацию о кол-ве гласных букв в фразах. Эта информация 
возвращается в виде списка словарей. Каждый элемент списка(словарь) соответствует фразе.

Примеры/Тесты:
    <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", False) -> True
    <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", True) -> (True, [{'а': 4}, {'а': 4}, {'а': 4}])
    <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> (True, [{'а': 4}, {'а': 2, 'у': 2}, {'а': 2, 'е': 1, 'о': 1}])
    <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> (False, [{'а': 4}, {'а': 2, 'у': 3}])
    <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> (False, [{'а': 11}, {'у': 6, 'а': 3}])
    <function_name>("Пам-парам-пурум Пум-пурум-карам") -> (True, [{'а': 3, 'у': 2}, {'у': 3, 'а': 2}])
'''
# РЕШЕНИЕ

# Импорт модулей
import re
import time
import random

# Функции
def inputRussianString(phrase):
    while True:
        string = input(phrase)
        if re.match(r'^[а-яА-ЯёЁ\s-]+$', string):
            count = sum(1 for word in string.split() if len(word) >= 2 and re.search(r'[аеёиоуыэюя]', word))
            if count >= 2:
                return string
            else:
                print('\033[31mОшибка!\033[0m Введите минимум два слова с гласными буквами.')
        else:
            print('\033[31mОшибка!\033[0m Допустимы только русские буквы, дефисы и пробелы.')

def printTypWriter(text, lagStart, lagEnd):
    time.sleep(lagStart)
    words = text.split() 
    count = 0 
    lineLength = 0 
    for word in words:
        wordLength = len(word)
        if lineLength + wordLength + 1 > 77: 
            print('\n', end='', flush=True) 
            count = 0 
            lineLength = 0 
        for char in word:
            print(char, end='', flush=True)
            time.sleep(0.1) 
        print(' ', end='', flush=True) 
        count += 1
        lineLength += wordLength + 1 
        if count == 10 or lineLength >= 75: 
            print('\n', end='', flush=True) 
            count = 0 
            lineLength = 0
    time.sleep(lagEnd) 
    print() 

def checkRhythm(text, inform):
    vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'} 
    phrases = text.lower().split()  
    tupleInf = ["количество гласных букв:"]  
    listInf = ["буквы:"]  
    rhythm = True    
    for phrase in phrases:  
        phrase = phrase.replace('-', '')  
        count = 0
        dict = {}
        for c in phrase: 
            if c in vowels:
                count += 1
                dict[c] = dict[c] + 1 if c in dict else 1
        tupleInf.append(count)  
        listInf.append(dict)        
        if len(set(tupleInf[1:])) > 1:  
            rhythm = False              
    if inform:  
        return rhythm, tupleInf, listInf  
    else:  
        return rhythm

# Код
hello = "\033[30mХорошо живёт на свете Винни Пух! Оттого поёт он эти песни вслух! И неважно, чем он занят, Если он толстеть не станет, А ведь он толстеть не станет НИКОГДА! ДА!\033[0m"

phrases = [
    "пара-ра-рам рам-пум-пупам па-ре-по-дам",
    "пара-ра-рам рам-пуум-пупам па-ре-по-дам",
    "Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па",    
    "пара-ра-рам рам-пам-папам па-ра-па-дам",    
    "Ба-бу-ба-бэй Ри-ра-рам-бэм Ту-ту-ту-тэй",
    "Пам-парам-пурум Пум-пурум-карам",      
    "Джи-джи-джэм-чем Ко-ко-ко-кэй Ча-ча-чам-дэм",    
    "Там-там-там Бам-бам-бам",
    "Там-пам-пам Рам-пам-пам",    
    "Таж-пам-пам Там-па-да-дам",
    "па-м-да-да па-да-да-дам",
    "па-да-да-да-дам па-ре-там-па-да-па-да-дам"
]

printTypWriter(hello, 0.1, 0.1)
choicePhrase = input('\033[34mВыберите способ ввода задания выражения:\033[0m\n\033[36m" 1 " - набор с клавиатуры\033[0m\n\033[35m" любой символ " - рандомно\033[0m : ')
choiceBool = input('\033[34mНадо ли возвращать полную информацию о кол-ве гласных букв в фразах:\033[0m\n\033[36m" 1 " - ДА\033[0m\n\033[35m" любой символ " - НЕТ\033[0m : ')
if choiceBool == '1':
    necessary = True
else:
    necessary = False
if choicePhrase == '1':
    phrase = inputRussianString('Введите выражение на русском языке: ')
    printTypWriter(phrase, 2, 1)       
    print(checkRhythm(phrase, necessary))
else: 
    random.shuffle(phrases) 
    for phrase in phrases:
        printTypWriter(phrase, 2, 1)        
        print(checkRhythm(phrase, necessary))
        