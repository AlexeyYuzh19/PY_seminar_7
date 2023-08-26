'''
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
Пример:
Ввод: `print_operation_table(lambda x, y: x * y) 
Вывод:
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
'''
# РЕШЕНИЕ

# Функции
def printTableFir(operation, num_rows=6, num_columns=6): 
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)] 
    for i in a: 
        print(*[f"\033[30m{x:>4}\033[0m" for x in i]) 

def printTableSec(operation, num_rows=6, num_columns=6):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"\033[30m{round(x, 1):>5}\033[0m" for x in i])  

# Код - вариант 1:
print("Вариант 1")
 
printTableFir(lambda x, y: x * y)

# Код - вариант 2:
print("Вариант 2")

operator = input('Введите операцию ("+", "-", "*", "/", "%", ">", "<", ">=", "<=", "==", "!=", "**", "//", "&", "|", "^", "<<", ">>", "and", "or") : ')
while operator not in ("+", "-", "*", "/", "%", ">", "<", ">=", "<=", "==", "!=", "**", "//", "&", "|", "^", "<<", ">>", "and", "or"): 
    print('\033[31mОшибка!\033[0m Введите операцию ("+", "-", "*", "/", "%", ">", "<", ">=", "<=", "==", "!=", "**", "//", "&", "|", "^", "<<", ">>", "and", "or") : ') 
    operator = input()   
printTableSec(eval(f"lambda x, y: x {operator} y"))
