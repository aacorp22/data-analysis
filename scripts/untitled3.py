# -*- coding: utf-8 -*-
"""
Created on Tue May 25 02:45:16 2021

@author: Admin
"""
import os

os.chdir("e:/work/")

import library as lib

# groups projects student_groups students_projects_tasks all_info
groups = lib.database.groups()
projects = lib.database.projects()
students_groups = lib.database.students_groups()
students_projects_tasks = lib.database.students_projects_tasks()
all_info = lib.database.all_info()


list1 = [0,48]
def delete_rows(dataframe, row_list):
    return dataframe.drop(dataframe.index[row_list])

df = delete_rows(all_info,list1 )
print(df)
# =============================================================================
# df.to_excel('./data/aaaaaaaaa.xlsx')
# =============================================================================
