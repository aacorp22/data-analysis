# -*- coding: utf-8 -*-
"""
Created on Mon May 24 19:41:23 2021

@author: Admin
"""
import pandas as pd
import os

os.chdir("e:/work/")

#IMPORT FROM EXCEL
#df = pd.read_excel("./data/all.xlsx")
df = pd.read_excel("./data/all.xlsx", index_col=("К_СТУ"))

"""
вывод одного столбца
"""
# =============================================================================
# def column(dataframe, column):
#     return (dataframe[[column]])
# 
# """
# вывод столбцов из списка
# """
# def columns(dataframe, list_of_columns):
#     return dataframe[list_of_columns]
# 
# spisok = ["ФАМ","ПРОЕКТ"]
# 
# students_projects = columns(df, spisok)
# students_projects.to_excel('./output/STUDENT_PROJECT.xlsx')
# 
# spisok2 = ["ФАМ","К_ГРУ","ПОЧТА_ГР"]
# 
# students_group_mail = columns(df, spisok2)
# students_group_mail.to_excel('./output/STUDENTS_GROUP_MAIL.xlsx')
# 
# spisok3 = ["ФАМ","К_ПРО","ПРОЕКТ","К_ЗАД"]
# students_project_task = columns(df, spisok3)
# students_project_task.to_excel('./output/PROJECTS_TASKS.xlsx')
# =============================================================================
#вывод строки в виде списка по индексу строчки датафрейма
#print(df.iloc[1].tolist())

#вывод строки в виде series по индексу строчки датафрейма

# =============================================================================
# def id_info(dataframe,student_id):
#     return(dataframe.loc[student_id])
# print(id_info(df, 47))
# =============================================================================
"""
тут я вывожу в свс принт колонки таблицы из списка, вывод как датафрейм
f = ['ФАМ', 'ПРОЕКТ', 'К_ЗАД']
print(df.to_excel(columns= f ,index=False))
"""
