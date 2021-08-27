#! usr/bin/env python
# -*- coding: utf-8 -*-


def print_columns(dataframe, list_of_columns):
    """
    Возвращает : датафрейм
    Параметры: датафрейм, список
    Функция принимает датафрейм и список
    из названий столбцов таблицы, затем возвращает 
    датафрейм ,состоящий только из указаннх столбцов
    """
	
def pivot_sort(dataframe, sort_list):
    """
    Возвращает: датафрейм
    Параметры: датафрейм, список
    Функция принимает датафрейм и список из 
    названий нужных столбцов таблицы ,
    затем возвращает сводную таблицу, отсортированную 
    по указанным в списке названиям
    """

def id_info(dataframe,id):
    """
    Возвращает: series
    Параметры: датафрейм, целое число
    Функция принимает датафрейм и число, 
    затем из таблицы отбирается строка, индекс
    которой равен заданному числу и выводится 
    как series
    """
    
def delete_cols(dataframe, list_of_cols):
    """
    Возвращает: датафрейм
    Параметры:датафрейм, список
    Функция удаляет указанные в списке столбцы
    из таблицы и возвращает новую таблицу в виде датафрейма
    без удаленных столбцов
    """
    
def show_head_part(dataframe, n):
    """
    Возвращает: датафрейм
    Параметры: датафрейм, целое число
    Функция выводит первые  n элементов указанного
    датафрейма и возвращает новую таблицу
    """
    
def show_tail_part(dataframe, n):
        """
    Возвращает: датафрейм
    Параметры: датафрейм, целое число
    Функция выводит последние  n элементов указанного
    датафрейма и возвращает новую таблицу
    """
 
 def columns_names_show(dataframe):
    """
    Возвращает: список
    Параметры: датафрейм
    Функция выводит названия всех столбцов 
    принятого датафрейма в список
    """
    
 def search_in_column(dataframe,column_name, searching_item):
    """
    Возвращает: датафрейм
    Параметры:датафрейм, строка, строка
    Функция ищет в указанном датафрейме 
    столбец с указанным названием и возвращает 
    датафрейм для указанного имени записи 
    в данном столбце
    """
    
def delete_rows(dataframe, row_list):
    """
    Возвращает: датафрейм
    Параметры: датафрейм, список
    Функция принимает список целых чисел, 
    затем удаляет из принятого датафрейма 
    строки с номерами, указанными в списке
    """