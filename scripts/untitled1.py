# -*- coding: utf-8 -*-
"""
Created on Mon May 24 22:45:38 2021

@author: Admin
"""

import pandas as pd
import os

os.chdir("e:/work/")

#IMPORT FROM EXCEL
#df = pd.read_excel("./data/all.xlsx")
df = pd.read_excel("./data/all.xlsx")
df2 = df.set_index("К_СТУ")

def extract(database_name):
    dataframe = pd.read_excel('./data/'+ database_name + '.xlsx')
    dataframe.index = dataframe.index + 1
    return dataframe

groups = extract("groups")
projects = extract("projects")
students_groups = extract("students_groups")
students_projects_tasks = extract("students_projects_tasks").set_index("К_СТУ")
all_info = extract('all').set_index("К_СТУ")

#a = pd.pivot_table(df2,index=["ПРОЕКТ","К_ГРУ","К_ЗАД"])

