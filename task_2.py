'''
6.2[32]: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента 
функцию, вычисляющую элемент по номеру строки и столбца, т.е. функцию двух аргументов. Аргументы num_rows и num_columns 
указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.
Примеры/Тесты:
print_operation_table(lambda x,y: x**y,4,4)
1   1   1   1
2   4   8  16
3   9  27  81
4  16  64 256

print_operation_table(lambda x,y: x*y)
1   2   3   4   5   6
2   4   6   8  10  12
3   6   9  12  15  18
4   8  12  16  20  24
5  10  15  20  25  30
6  12  18  24  30  36
(*) Усложнение. Сформируйте форматированный вывод с номерами строк и столбцов

Примеры/Тесты:
print_operation_table(lambda x,y: x**y,4,4)
       1   2   3   4
    ----------------
1 |    1   1   1   1
2 |    2   4   8  16
3 |    3   9  27  81
4 |    4  16  64 256

print_operation_table(lambda x,y: x*y)
       1   2   3   4   5   6
    ------------------------
1 |    1   2   3   4   5   6
2 |    2   4   6   8  10  12
3 |    3   6   9  12  15  18
4 |    4   8  12  16  20  24
5 |    5  10  15  20  25  30
6 |    6  12  18  24  30  36
'''
# РЕШЕНИЕ

# Функции
def positiveInteger(phrase):
    while True:
        try:
            posIn = int(input(f"Введите {phrase} : "))
            if posIn <= 0:
                print("\033[31mОшибка!\033[0m Значение должно быть больше нуля.")                 
                continue 
            break           
        except ValueError:
            print("\033[31mОшибка!\033[0m Введено не целое число.") 
    return posIn

def printTableFir(operation, a, b): 
    c = [[operation(i, j) for j in range(1, b + 1)] for i in range(1, a + 1)] 
    for i in c: 
        print(*[f"\033[30m{x:>5}\033[0m" for x in i]) 

def printTableSec(operation, a, b):    
    print("        ", end="")
    for j in range(1, b + 1):
        print(f"{j:6}", end="")
    print("\n " + "--" * (b * 4))
    for i in range(1, a + 1):
        print(f"{i:>6} |", end="")
        for j in range(1, b + 1):
            print(f"\033[30m{round(operation(i, j), 1):>6}\033[0m", end="")
        print()

# Код - вариант 1:
print("Вариант 1")
 
printTableFir(lambda x, y: x ** y, 4, 4)

# Код - вариант 2:
print("Вариант 2")

num_rows = positiveInteger("количество строк")
num_columns = positiveInteger("количество столбцов")
operator = input('Бинарная операция ("+", "-", "*", "/", "%", ">", "<", ">=", "<=", "==", "!=", "**", "//", "&", "|", "^", "<<", ">>", "and", "or") : ')
while operator not in ("+", "-", "*", "/", "%", ">", "<", ">=", "<=", "==", "!=", "**", "//", "&", "|", "^", "<<", ">>", "and", "or"): 
    print('\033[31mОшибка!\033[0m Бинарная операция ("+", "-", "*", "/", "%", ">", "<", ">=", "<=", "==", "!=", "**", "//", "&", "|", "^", "<<", ">>", "and", "or") : ') 
    operator = input()   
printTableSec(eval(f"lambda x, y: x {operator} y"), num_rows, num_columns)
