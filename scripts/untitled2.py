# -*- coding: utf-8 -*-
"""
Created on Tue May 25 02:15:46 2021

@author: Admin
"""

#IMPORT FROM EXCEL
#df = pd.read_excel("./data/all.xlsx")

def extract(database_name):
    dataframe = pd.read_excel('./data/'+ database_name + '.xlsx')
    dataframe.index = dataframe.index + 1
    return dataframe

all_info = extract('all').set_index("К_СТУ")
groups = extract("groups")
projects = extract("projects")
students_groups = extract("students_groups")
students_projects_tasks = extract("students_projects_tasks").set_index("К_СТУ")

