from tkinter import ttk
import tkinter as tki
import csv
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import sys
from pathlib import Path
sys.path.append(f'{Path().absolute().parent}\Library')
from database import dirchoose, datachoose
from pathselect import Ways, ways

def initializeMainWindow():
    """
    Автор: Азизбек Пардаев
    -----------------------
    Создание главного окна приложения
    
    Ничего не возвращает
    """
    dirchoose(directoryWay)
    dirchoose(graphWay)
    global Data
    Data = datachoose(baseWay)
    global win_main
    win_main = Window()
    frameForDataOperations = tki.Frame(win_main)
    frameForDataOperations.pack()
    label_buttons = tki.Label(frameForDataOperations, text = "Действия над таблицей", font = "Arial 9")
    label_buttons.pack(side=tki.TOP)
    
    button_add = tki.Button(frameForDataOperations, text = "Добавить",
                            width = 10, height = 1, command = knopka_dobavit)
    button_add.pack(side=tki.LEFT, padx=10, pady=10)
    
    button_sort = tki.Button(frameForDataOperations, text = "Текстовый отчет",
                             width = 14, height = 1, command = text_otchet)
    button_sort.pack(side=tki.LEFT, padx=10, pady=10)
    
    def udalenie():
        """
        Автор: Лазизбек Камаров
        -----------------------
        Удаление выбранных строк из базы данных и сохранение обновленной базы
        
        Ничего не возвращает
        """
        global Data
        
        if win_main.mainObj.selectedNumber > 0:
            for selectedItem in win_main.mainObj.tree.selection():
                children = list(map(int, win_main.mainObj.tree.get_children()))
                for iid in children:
                    if win_main.mainObj.tree.item(iid)['text'] == win_main.mainObj.tree.item(selectedItem,"text"): 
                        Data = Data.drop(Data.index[children.index(iid)])
                        break
                win_main.mainObj.tree.delete(selectedItem)
                win_main.mainObj.baseLength = win_main.mainObj.baseLength - 1
            Data.to_excel(baseWay,index=False)
    button_delete = tki.Button(frameForDataOperations, text = "Удалить",
                               width = 10, height = 1,
                               command = udalenie)
    button_delete.pack(side=tki.LEFT, padx=10, pady=10)
    
    def checkSelectedAndChange():
        """
        Автор: Солтан Массоуд
        -----------------------
        Вызов изменения выбранной пользователем строки
        
        Ничего не возвращает
        """
        if len(win_main.mainObj.tree.selection()) == 1:
            position = -1
            idOfRow = -1
            selectedItem = win_main.mainObj.tree.selection()[0]
            children = list(map(int, win_main.mainObj.tree.get_children()))
            for iid in children:
                if win_main.mainObj.tree.item(iid)['text'] == win_main.mainObj.tree.item(selectedItem,"text"): 
                    position = children.index(iid)
                    idOfRow = win_main.mainObj.tree.item(iid)['text']
                    break
            izmenit(position, idOfRow)
        else:
            tki.messagebox.showinfo("Ошибка", "Одновременно изменять можно ровно одну строку")
    button_change = tki.Button(frameForDataOperations, text = "Изменить",
                             width = 10, height = 1, command = checkSelectedAndChange)
    button_change.pack(side=tki.LEFT, padx=10, pady=10)
    frameForPlots = tki.LabelFrame(win_main, text = "Создание графического отчёта")
    frameForPlots.pack()
    comboChoosePlot = ttk.Combobox(frameForPlots, state="readonly", width=60,
                            values=['Количество студентов в проектах',
                                    'График сложности заданий в проектах',
                                    'Почты групп'])
    comboChoosePlot.current(0)
    comboChoosePlot.pack()
    
    def checkSelected():
        """ 
        Автор: Солтан Массоуд
        -----------------------
        Функция для построения графика при нажатии на кнопку Построить

        Ничего не возвращает
        """
        postroyka_grafika(comboChoosePlot.get())
    button_graphs = tki.Button(frameForPlots, text = "Построить", width = 10, height = 1, command = checkSelected)
    button_graphs.pack()
    
    btn_exit = tki.Button(win_main, text='Выход', height=1, command=win_main.destroy, cursor='hand2')
    btn_exit.pack()
    win_main.mainloop()

def perviy(data):
    """
    Автор: Лазизбек Камаров
    -----------------------
    График количества студентов по проектам
    
    Параметры
    ----------
    датафрейм
    
    Ничего не возвращает

    """
    fig = plt.figure()
    Plot = fig.add_subplot()
    Plot.set_title('Количество студентов в проектах', color = 'Blue')
    Plot.hist(Data['Проект'])
    Plot.set_xlabel('Проекты',color = 'Blue')
    Plot.set_ylabel('Количество студентов',color = 'Blue')
    plt.yticks(color = 'orange')
    plt.xticks(rotation = 75, color = 'orange')    
    plt.tight_layout()
    way= graphWay + "/first_graph.png"
    fig.savefig(f"{way}")
    plt.show()
    
def vtoroy(data):
    """
    Автор: Азизбек Пардаев
    -----------------------
    График сложности заданий в проектах
    
    Параметры
    ----------
    датафрейм
    
    Ничего не возвращает

    """
    alpha = sorted(data['Код проекта'].unique())
    beta = sorted(data['Код задания'].unique())
    beta = beta[0:10]
    df2 = pd.DataFrame(
        {'Код проекта': alpha,
          'Код задания': beta})
    df2.plot.barh(x='Код проекта',y='Код задания', xlabel = 'Код проекта')
    
def tretiy(data):
    alpha = sorted(data['Код группы'].unique())
    beta = sorted(data['Почта группы'].unique())[0:8]
    plt.title('Почты групп', color = 'blue')
    plt.xlabel('Код группы',color = 'blue')
    plt.ylabel('Почта группы',color = 'blue')
    plt.yticks(color = 'orange')
    plt.xticks(color = 'orange')
    plt.stem(alpha,beta,  use_line_collection=True)
    plt.tight_layout()
    plt.show()
    
class sozdaniye_tablisi(object):
    """
    Автор: Лазизбек Камаров
    -----------------------
    Класс для создания сводной таблицы

    """
    def __init__(self, way, length, app, code):
        """
        Автор: Лазизбек Камаров
        -----------------------
        Устанавливает все необходимые атрибуты для объекта sozddniye_tablisi
    
        Параметры
        ----------
         way : название файла с базой данных,строка
         length : количество столбцов в таблице,строка
         app : название ttk.Treeview окна,строка
         code : название кодировки (в проекте 'utf-8'),строка 
        """
        i = 0
        self.selectedNumber = -1
        self.way = way
        with open(way, 'r', encoding=code) as f1:
            reader = csv.reader(f1, delimiter=',')
            row1 = next(reader)
            columns_from_table = list(row1)       
            length = len(columns_from_table)
            columns_default = []
            for i in range(length):
                columns_default.append(f"#{i+1}")
            scrollbar = ttk.Scrollbar(app)

            self.tree = ttk.Treeview(app, padding=3, show="headings", columns=columns_default,
                                        yscrollcommand=scrollbar.set)
            scrollbar.config(command=self.tree.yview)
            scrollbar.pack(side=tki.RIGHT, fill=tki.Y)
            i = 0
            for i in range(length):
                self.tree.heading(columns_default[i], text=columns_from_table[i])
            i = 0
            self.baseLength = 0
        with open(way, 'r', encoding=code) as f1:
            reader = csv.reader(f1, delimiter=',')
            for row in reader:
                i = i + 1
                if i!=1:
                    self.tree.insert("", 'end', iid=i-2, text=i-2, values=row)
                    self.baseLength = self.baseLength + 1
                if i==2:
                    self.tree.bind("<<TreeviewSelect>>", self.number_of_selected)
    def number_of_selected(self, event):
        """
        Автор: Лазизбек Камаров
        -----------------------
        Считает количество элементов, выбранных для удаления

        """
        self.selectedNumber = len(self.tree.selection())
        
def knopka_dobavit():
    """
    Автор: Азизбек Пардаев
    -----------------------
    Обработка нажатия кнопки Добавить

    """
    win_new = tki.Toplevel()
    win_new.title("Добавление записи")  
    frameForInput = tki.Frame(win_new)
    frameForButtons = tki.Frame(win_new)
    btn_exit = tki.Button(frameForButtons, text='Выход', command=win_new.destroy, cursor='hand2')
    frameForInput.pack()
    label_1 = tki.Label(frameForInput, text = "Количество строк: ")
    label_1.pack(side=tki.LEFT, padx=10, pady=10)
    entry_1 = tki.Entry(frameForInput, width = 4)
    entry_1.pack(side=tki.LEFT, padx=10, pady=10)
    
    def input_data():
        """
        Автор: Азизбек Пардаев
        -----------------------
        Ввод новых данных и проверка их на корректность
        
        """
        flag = False
        size = 0
        try :
            size = int(entry_1.get())
            if(size<=0):
                flag = True
        except ValueError:
            flag = True
        
        if flag == True:
            entry_1.delete( 0, 'end')
            tki.messagebox.showinfo("Ошибка", "Проверьте правильность введённых данных")
        elif int(entry_1.get())>20:
            tki.messagebox.showinfo("Информация", "Одновременно можно добавлять не более 20 строк")
        else:
            def update_table():
                """
                Автор: Азизбек Пардаев
                -----------------------
                Обновление базы данных 
                
                """
                flag = False
                for i in range(kol_rows-1):
                    try :
                        int(student[i].get())
                    except ValueError:
                        flag = True
                        student[i].delete( 0, 'end')
                    try :
                        number = int(projectcode[i].get())
                        if(number<=0):
                            flag = True
                            projectcode[i].delete( 0, 'end')
                    except ValueError:
                        flag = True
                        projectcode[i].delete( 0, 'end')
                if flag == False:
                    bufferList = []
                    way= baseWay
                    for i in range(kol_rows-1):
                        buffer = []
                        buffer.append(student[i].get())
                        buffer.append(fam[i].get())
                        buffer.append(group[i].get())
                        buffer.append(email[i].get())
                        buffer.append(project[i].get())
                        buffer.append(projectcode[i].get())
                        buffer.append(task[i].get())
                        bufferList.append(buffer)
                    lastEl = list(map(int, win_main.mainObj.tree.get_children()))[-1]
                    with open(way, "a+", newline='\n', encoding='utf-8') as csv_file:
                        writer = csv.writer(csv_file, delimiter=',')
                        for i in range(kol_rows-1):
                            writer.writerow(bufferList[i])
                            win_main.mainObj.tree.insert('', 'end',iid=lastEl+1+i, text=lastEl+1+i, values=bufferList[i])
                            win_main.mainObj.baseLength = win_main.mainObj.baseLength + 1
                    datachoose(baseWay)
                    win_new_next.destroy()
                    tki.messagebox.showinfo("Информация", "База данных обновлена")
                else:
                    tki.messagebox.showinfo("Ошибка", "Проверьте правильность введённых данных")
            kol_rows = int(entry_1.get()) + 1
            win_new.destroy()
            win_new_next = tki.Tk()
            win_new_next.title("Внесение данных")
            win_new_next.geometry("930x500")  

            frameForTableAndScroll = tki.LabelFrame(win_new_next, text="Внесение данных")
            canvas = tki.Canvas(frameForTableAndScroll)
            f = tki.Frame(canvas)
            scrollbar = tki.Scrollbar(frameForTableAndScroll, command=canvas.yview)
            
            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.pack(side=tki.LEFT, fill=tki.BOTH, expand=True)
            scrollbar.pack(side=tki.RIGHT, fill=tki.BOTH)
            f.pack(fill=tki.BOTH, expand=True)
            def onFrameConfigure(event):
                """
                Автор: Азизбек Пардаев
                -----------------------
                Вывод в отдельном окне
        
                """
                canvas.configure(scrollregion=f.bbox('all'))
    
            def onCanvasConfigure(event):
                """
                Автор: Азизбек Пардаев
                -----------------------
                Вывод окна
                
                """
                canvas.itemconfigure(_frame_id, width=canvas.winfo_width())
            _frame_id = canvas.create_window(
                                     canvas.winfo_width(), 0,
                                     anchor='nw',
                                     window=f)
            f.bind('<Configure>', onFrameConfigure)
            canvas.bind('<Configure>', onCanvasConfigure)
            width = 7 
            labelList = []
            labelList.append(tki.Label(f, text="Код студента"))
            labelList.append(tki.Label(f, text="Фамилия"))
            labelList.append(tki.Label(f, text="Код группы"))
            labelList.append(tki.Label(f, text="Почта группы"))
            labelList.append(tki.Label(f, text="Проект"))
            labelList.append(tki.Label(f, text="Код проекта"))
            labelList.append(tki.Label(f, text="Код задания"))
            #Массивы для полей вводимых данных
            student = []
            fam = []
            group = []
            email = []
            project = []
            projectcode = []
            task = []
             
            for i in range(kol_rows): #Rows
                for j in range(width): #Columns
                    if i == 0:
                        labelList[j].grid(row=i, column=j)
                    else:
                        if j ==0:
                            student.append(tki.Entry(f, text=""))
                            student[i-1].grid(row=i, column=j)
                        elif j ==1:
                            fam.append(tki.Entry(f, text=""))
                            fam[i-1].grid(row=i, column=j)
                        elif j ==2:
                            group.append(tki.Entry(f, text=""))
                            group[i-1].grid(row=i, column=j)
                        elif j ==3:
                            email.append(ttk.Combobox(f, state="readonly", 
                                     values=['1@miem.hse.ru','1@edu.hse.ru',
                                                '2@miem.hse.ru','2@edu.hse.ru',
                                                '3@miem.hse.ru','3@edu.hse.ru',
                                                '4@miem.hse.ru','4@edu.hse.ru',
                                                '5@miem.hse.ru','5@edu.hse.ru',
                                                '6@miem.hse.ru','6@edu.hse.ru',
                                                '7@miem.hse.ru','7@edu.hse.ru',
                                                '8@miem.hse.ru','8@edu.hse.ru']))
                            email[i-1].current(0)
                            email[i-1].grid(row=i, column=j)
                        elif j ==4:
                            # project.append(tki.Entry(f, text=""))
                            # project[i-1].grid(row=i, column=j)
                            project.append(ttk.Combobox(f, state="readonly", 
                            values=['Медиацентр','Робототехника',
                                    'Майнинг','Лазерная резка',
                                    'Ардуино','Линукс',
                                    'Веб сайт','Чат-бот',
                                    'Чат-бот','Разработка игры',
                                    'Web дизайн']))
                            project[i-1].current(0)
                            project[i-1].grid(row=i, column=j)
                        elif j ==5:
                            projectcode.append(tki.Entry(f, text=""))
                            projectcode[i-1].grid(row=i, column=j)
                        elif j ==6:
                            task.append(ttk.Combobox(f, state="readonly", 
                                    values=['1',
                                                '2',
                                                '3',
                                                '4',
                                                '5',
                                                '6',
                                                '7',
                                                '8',
                                                '9',
                                                '10',
                                                '11']))
                            task[i-1].current(0)
                            task[i-1].grid(row=i, column=j)
            frameForTableAndScroll.pack(expand=True, fill=tki.BOTH)
            button_update = tki.Button(win_new_next, text = "Обновить базу данных", height = 1, command = update_table)
            button_update.pack(side=tki.BOTTOM)
            button_exit = tki.Button(win_new_next, text='Выход', height=1, command=win_new_next.destroy, cursor='hand2')
            button_exit.pack(side=tki.BOTTOM)
            win_new_next.mainloop()
               
    button_input = tki.Button(frameForButtons, text = "Ок", command = input_data)
    frameForButtons.pack()
    btn_exit.pack(side=tki.LEFT, padx=10, pady=10)
    button_input.pack(side=tki.LEFT, padx=10, pady=10)
    
    win_new.mainloop()

def izmenit(position, idOfRow):
    """
        Автор: Солтан Массоуд
        -----------------------
        Изменение одной строки базы данных 
        
        """
    def update_table(): 
        """
        Автор: Солтан Массоуд
        -----------------------
        Обновление базы данных после изменения 
                
        """
        flag = False
        try :
            int(studentEntry.get())
        except ValueError:
            flag = True
            studentEntry.delete( 0, 'end')
        try :
            number = int(projectcodeEntry.get())
            if(number<=0):
                flag = True
                projectcodeEntry.delete( 0, 'end')
        except ValueError:
            flag = True
            projectcodeEntry.delete( 0, 'end')
        if flag == False:
            buffer = []
            buffer.append(studentEntry.get())
            buffer.append(famEntry.get())
            buffer.append(groupEntry.get())
            buffer.append(emailEntry.get())
            buffer.append(projectEntry.get())
            buffer.append(projectcodeEntry.get())
            buffer.append(taskEntry.get())
            for j in range(len(buffer)):
                Data.values[position][j] = buffer[j]
            Data.to_csv(baseWay, sep=",", index=False)
            win_main.mainObj.tree.item(idOfRow, values=buffer)
            win_new_next.destroy()
            tki.messagebox.showinfo("Информация", "База данных обновлена")
        else:
            tki.messagebox.showinfo("Ошибка", "Проверьте правильность введённых данных")
    kol_rows = 2
    win_new_next = tki.Tk()
    win_new_next.title("Изменение базы данных")
    win_new_next.geometry("930x500")  
    # --- create canvas with scrollbar ---
    frameForTableAndScroll = tki.LabelFrame(win_new_next, text="Изменение данных")
            
            
    canvas = tki.Canvas(frameForTableAndScroll)
    f = tki.Frame(canvas)
    scrollbar = tki.Scrollbar(frameForTableAndScroll, command=canvas.yview)
            
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side=tki.LEFT, fill=tki.BOTH, expand=True)
    scrollbar.pack(side=tki.RIGHT, fill=tki.BOTH)
    f.pack(fill=tki.BOTH, expand=True)
    def onFrameConfigure(event):
        """
        Автор: Солтан Массоуд
        -----------------------
        Вывод отчета в отдельном окне
        
        """
        canvas.configure(scrollregion=f.bbox('all'))
    
    def onCanvasConfigure(event):
        """
        Автор: Солтан Массоуд
        -----------------------
        Вывод отчёта
                
        """
        canvas.itemconfigure(_frame_id, width=canvas.winfo_width())
    _frame_id = canvas.create_window(
                                     canvas.winfo_width(), 0,
                                     anchor='nw',
                                     window=f)
    f.bind('<Configure>', onFrameConfigure)
    canvas.bind('<Configure>', onCanvasConfigure)
    width = 7 
    labelList = []
    labelList.append(tki.Label(f, text="Код студента"))
    labelList.append(tki.Label(f, text="Фамилия"))
    labelList.append(tki.Label(f, text="Код группы"))
    labelList.append(tki.Label(f, text="Почта группы"))
    labelList.append(tki.Label(f, text="Проект"))
    labelList.append(tki.Label(f, text="Код проекта"))
    labelList.append(tki.Label(f, text="Код задания"))
             
    for i in range(kol_rows): #Rows
        for j in range(width): #Columns
            if i == 0:
                labelList[j].grid(row=i, column=j)
            else:
                if j ==0:
                    studentEntry = tki.Entry(f)
                    studentEntry.insert(0,Data.values[position][j])
                    studentEntry.grid(row=i, column=j)
                elif j ==1:
                    famEntry=(tki.Entry(f))
                    famEntry.insert(0,Data.values[position][j])
                    famEntry.grid(row=i, column=j)
                elif j ==2:
                    groupEntry=(tki.Entry(f))
                    groupEntry.insert(0,Data.values[position][j])
                    groupEntry.grid(row=i, column=j)
                elif j ==3:
                    emailEntry=(ttk.Combobox(f, state="readonly", 
                                        values=['1@miem.hse.ru','1@edu.hse.ru',
                                                '2@miem.hse.ru','2@edu.hse.ru',
                                                '3@miem.hse.ru','3@edu.hse.ru',
                                                '4@miem.hse.ru','4@edu.hse.ru',
                                                '5@miem.hse.ru','5@edu.hse.ru',
                                                '6@miem.hse.ru','6@edu.hse.ru',
                                                '7@miem.hse.ru','7@edu.hse.ru',
                                                '8@miem.hse.ru','8@edu.hse.ru']))
                    if Data.values[position][j] == '@miem.hse.ru':
                        emailEntry.current(0)
                    else:
                        emailEntry.current(1)
                    emailEntry.grid(row=i, column=j)
                elif j ==4:
                    projectEntry=(tki.Entry(f))
                    projectEntry.insert(0,Data.values[position][j])
                    projectEntry.grid(row=i, column=j)
                elif j ==5:
                    projectcodeEntry=(tki.Entry(f))
                    projectcodeEntry.insert(0,Data.values[position][j])
                    projectcodeEntry.grid(row=i, column=j)
            
                elif j ==6:
                    taskEntry=(tki.Entry(f))
                    taskEntry.insert(0,Data.values[position][j])
                    taskEntry.grid(row=i, column=j)
             
                    
    frameForTableAndScroll.pack(expand=True, fill=tki.BOTH)
    button_update = tki.Button(win_new_next, text = "Обновить базу данных", height = 1, command = update_table)
    button_update.pack(side=tki.BOTTOM)
    button_exit = tki.Button(win_new_next, text='Выход', height=1, command=win_new_next.destroy, cursor='hand2')
    button_exit.pack(side=tki.BOTTOM)
    win_new_next.mainloop()

def text_otchet():
    """
    Автор: Лазизбек Камаров
    -----------------------
    Обработка нажатия кнопки Текстовый отчет
    
    """
    win_new = tki.Tk()
    win_new.title("Текстовый отчет")
    win_new.geometry("400x300+450+250")
    btn_exit = tki.Button(win_new, text='Выход', font=('Arial', 15), bg='grey', fg='yellow', height=1, width=10, command=win_new.destroy, cursor='hand2')
    btn_exit.pack(side = "bottom")
    
    label_1 = tki.Label(win_new, text = "Выберите отчет")
    label_1.place(relx=.1, rely=.1)
    comboExample = ttk.Combobox(win_new, state="readonly", width=30,
                            values=['Сортировка студентов по проектам',
                                    'Количество студентов в проекте',
                                    'Участие в нескольких проектах',
                                    'Досье на каждого студента',
                                    'Почтовые адреса для связи'])
    comboExample.current(0)
    comboExample.place(relx=.4, rely=.1)
    
    def  vibor_otcheta():
            """
            Автор: Азизбек Пардаев
            -----------------------
            Выбор вида отчета
            
            Возвращает
            -------
            Измененную/новую сводную таблицу, сохраненную в csv файл 
        
            """
            
            length = 0
            win_table = tki.Toplevel(win_main)
            frame_tabels = ttk.LabelFrame(win_table, text =comboExample.get()) 
            if comboExample.get() == 'Сортировка студентов по проектам':
                tki.messagebox.showinfo("Информация", "Отсортированный файл сохранён в Фамилии_проекты.csv")
                NUM1 = Data[['Код проекта','Фамилия','Проект']].sort_values('Код проекта')
                way= directoryWay + "/Фамилии_проекты.csv"
                NUM1.to_csv(f"{way}", sep = ",", index=False)
            elif comboExample.get() == 'Количество студентов в проекте':
                tki.messagebox.showinfo("Информация", "Отсортированный файл сохранён в Количество_студентов_по_проектам.csv")
                way= directoryWay + "/Количество_студентов_по_проектам.csv"
                NUM2 = Data.pivot_table(index=['Проект'], aggfunc='size')
                NUM2 = pd.DataFrame(NUM2).reset_index()
                NUM2.columns = ['Проект', 'Количество студентов']
                NUM2.to_csv(f"{way}", sep = ",", index=False)
            elif comboExample.get() == 'Участие в нескольких проектах':
                tki.messagebox.showinfo("Информация", "Отсортированный файл сохранён в Участие_в_нескольких_проектах.csv")
                NUM3= Data.groupby(['Фамилия','Почта группы']).count()
                NUM3 = NUM3[NUM3['Код студента'] > 1]
                NUM3= NUM3['Код студента']
                NUM3 = pd.DataFrame(NUM3).reset_index()
                NUM3.columns = ['Фамилия','Почта группы','Участий в проектах']
                way= directoryWay + "/Участие_в_нескольких_проектах.csv"
                NUM3.to_csv(f"{way}", sep=",", index=False)
            elif comboExample.get() == 'Досье на каждого студента':
                tki.messagebox.showinfo("Информация", "Отсортированный файл сохранён в Досье_студентов.csv")
                NUM4 = Data.stack()
                way= directoryWay + "/Досье_студентов.csv"
                NUM4.to_csv(f"{way}", sep=",", index=False)
            elif comboExample.get() == 'Почтовые адреса для связи':
                tki.messagebox.showinfo("Информация", "Отсортированный файл сохранён в Студенты_почта.csv")
                NUM5 =Data[['Код группы','Фамилия','Почта группы']].sort_values('Почта группы')
                way= directoryWay + "/Студенты_почта.csv"
                NUM5.to_csv(f"{way}", sep = ",", index=False)                    
            mainObj = sozdaniye_tablisi(way, length, frame_tabels, 'utf-8')
            mainTree = mainObj.tree
            mainTree.pack(side=tki.BOTTOM, fill=tki.BOTH, expand=tki.YES)
            frame_tabels.pack()  # положение
            win_new.destroy()
            win_table.lift()
            win_table.mainloop()
            
    button_OK = tki.Button(win_new, text='Ок', height=1, width=10, command=vibor_otcheta, cursor='hand2')
    button_OK.place(relx=.4, rely=.2)
    
    win_new.mainloop()

def postroyka_grafika(selected):
    """
    Автор: Солтан Массоуд
    -----------------------
    Построение графиков №1 №2 №3 из comboChoosePlot
    
    Параметры
    ----------
    selected : str
                название графика из comboChoosePlot
                
    Возвращает
    -------
    график в отдельном окне

    """
    global fig
    if selected == 'Количество студентов в проектах':
        fig = perviy(Data)
    elif selected == 'График сложности заданий в проектах':
        fig = vtoroy(Data)
    elif selected == 'Почты групп':
        fig = tretiy(Data)

class Window(tki.Tk):
    """
    Автор: Лазизбек Камаров
    -----------------------
    Класс для создания окна Tk()

    """
    def __init__(self):
        """
        Устанавливает все необходимые атрибуты для объекта Window
        
        """
        super(Window, self).__init__()
        self.frame_tabels = ttk.LabelFrame(self, text = 'Загруженная база данных')
        self.title("Project Python")
        length = 0
        self.mainObj = sozdaniye_tablisi(baseWay, length, self.frame_tabels, 'utf-8')
        self.mainTree = self.mainObj.tree
        self.mainTree.pack(side=tki.BOTTOM, fill=tki.BOTH, expand=tki.YES)
        self.frame_tabels.pack()
Ways()
if(len(ways) == 3):
    global directoryWay
    global graphWay
    global baseWay
    directoryWay = ways[0]
    graphWay = ways[1]
    baseWay = ways[2]
    initializeMainWindow()