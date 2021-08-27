import os
import pandas as pd
def dirchoose(way):
    """
    Автор: Солтан Массоуд
    -----------------------
    Выбор папки для хранения файлов
    
    Параметры
    ----------
    way - строка

    Ничего не возвращает
    """
    os.getcwd()
    os.chdir(way)

def datachoose(way):
    """
    Автор: Азизбек Пардаев
    -----------------------
    Выбор файла с базой данных
    
    Параметры
    ----------
    way - строка

    Возвращает
    -------
    Датафрейм

    """
    assert os.path.isfile(way)
    checkfile(way)
    global Data
    Data = pd.read_csv(way, delimiter=',', encoding='utf-8')
    return Data

def checkfile(way):
    """
    Автор: Солтан Массоуд 
    -----------------------
    Проверка на наличие '/n' в файле с базой данных
    
    Параметры
    ----------
    way - строка

    Ничего не возвращает

    """
    with open(way,'r', encoding='utf-8') as file:
        data = file.readlines() 
        lastRow = data[-1]
        lastChar = lastRow[-1]
        if(lastChar != '\n'):
            makefile(way, Data)

def makefile(way, Data):
    """
    Автор: Лазизбек Камаров
    -----------------------
    Добавление '/n' в файл с базой данных для корректного чтения данных
    
    Параметры
    ----------
    way : строка
    Data : датафрейм

    Ничего не возвращает
    """
    with open(way,'a', encoding='utf-8') as fd:
        fd.write('\n')
