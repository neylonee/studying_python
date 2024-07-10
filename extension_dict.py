import os
# Найдите в стандартной библиотеке Python пакет для вывода со-
# держимого каталогов. Используйте этот пакет и напишите функ-
# цию, которая получает имя каталога, получает список всех файлов
# в этом каталоге и выводит отчет с количеством файлов для каждо-
# го расширения.
def in_catalog(catalog_name):
    list = os.listdir(name)
    res = {}
    for extension in list:
        extension = extension[extension.find('.'):]
        res.setdefault(extension,0)
        res[extension]+=1
    return res
print(in_catalog('your_catalog_name'))
