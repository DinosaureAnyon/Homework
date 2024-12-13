print('\n#1')


def read_last(lines, file):
    abstract_file = open('article.txt', 'r', encoding='utf-8')
    for n in range(lines):
        print(abstract_file.readline(), end='')


n = int(input('Input int positive number: '))
file = open('article.txt', 'r', encoding='utf-8')
rows_number = len(file.readlines())
if n > 0 and n < rows_number:
    read_last(n, file)


import os


def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
        print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([file for file in catalog[2]])}')
        print('-' * 40)


print_docs('C:/Users/User/Downloads/2')


print('\n#3')
from functools import reduce


def longest_words(file):
    rows = file.readlines()
    words = reduce(lambda x, y: x[:-1] + ' ' + y, rows).split()
    max_len_word = max(map(len, words))
    return list(filter(lambda x: len(x) == max_len_word, words))


file = open('article.txt', 'r', encoding='utf-8')
print(longest_words(file))


print('\n#4')
name = input('Введите имя файла: ') + '.txt'
file = open(name, "w")
s = input('Введите строку (для завершения нажмите ENTER): ') + '\n'
while len(s) > 1:
    file.write(s)
    s = input('Введите строку (для завершения нажмите ENTER): ') + '\n'
print('Работа с файлом окончена')