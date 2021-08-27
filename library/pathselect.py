import tkinter as tki
from tkinter import filedialog
global ways
global directoryWay
ways = []
def Ways():
    """
    Автор: Лазизбек Камаров
    -----------------------
    Окно для выбора папки проекта и файла с базой данных
    
    Ничего не возвращает
    """
    choose_way = tki.Tk()
    choose_way.title("Project Python")

    
    def folder():
        """
        Автор: Азизбек Пардаев
        -----------------------
        Отображение названия директории, выбранной пользователем, в поле EntryDir окна choose_way
    
        Ничего не возвращает
        """
        global directoryWay
        directory = filedialog.askdirectory(initialdir = "/",title = "Select directory")
        directoryWay = directory
        entryDir.config(state = "normal")
        entryDir.delete(0, 'end')
        entryDir.insert(tki.END, directoryWay)
        entryDir.config(state = "readonly")
    
    def database():
        """
        Автор: Лазизбек Камаров
        -----------------------
        Отображение названия файла с базой данных

        Ничего не возвращает
        """
        global baseWay
        filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        baseWay = filename
        entryBase.config(state = "normal")
        entryBase.delete(0, 'end')
        entryBase.insert(tki.END, baseWay)
        entryBase.config(state = "readonly")
    
    def graphs():
        """
        Автор: Солтан Массоуд
        -----------------------
        Отображение названия директории, выбранной пользователем

        Ничего не возвращает
        """
        global graphWay
        graph = filedialog.askdirectory(initialdir = "/",title = "Select directory")
        graphWay = graph
        entryGraph.config(state = "normal")
        entryGraph.delete(0, 'end')
        entryGraph.insert(tki.END, graphWay)
        entryGraph.config(state = "readonly")
    
    frameForDirectories = tki.Frame(choose_way)
    frameForDirectories.pack()
    labelDir = tki.Label(frameForDirectories, text = "Выберите рабочую директорию для сохранения файлов", font = "Arial 11", fg="black")
    labelDir.pack()
    entryDir = tki.Entry(frameForDirectories, width = 40, state = 'readonly')
    entryDir.pack()
    buttonDir = tki.Button(frameForDirectories, text = "Выбрать", command = folder)
    buttonDir.pack()
    labelGraph = tki.Label(frameForDirectories, text = "Выберите рабочую директорию для сохранения графиков", font = "Arial 11", fg="black")
    labelGraph.pack()
    entryGraph = tki.Entry(frameForDirectories, width = 40, state = 'readonly')
    entryGraph.pack()
    buttonGraph = tki.Button(frameForDirectories, text = "Выбрать", command = graphs)
    buttonGraph.pack()
    labelBase = tki.Label(frameForDirectories, text = "Выберите нужную базу данных", font = "Arial 11", fg="black")
    labelBase.pack()
    entryBase = tki.Entry(frameForDirectories, width = 40, state = 'readonly')
    entryBase.pack()
    buttonBase = tki.Button(frameForDirectories, text = "Выбрать", command = database)
    buttonBase.pack()

    def checkWays():
        """
        Автор: Азизбек Пардаев
        -----------------------
        Проверка полей entryDir и entryBase на наличие данных и переход к главному окну приложения

        Ничего не возвращает
        """
        if entryDir.get() == "" or entryBase.get()== "":
            tki.messagebox.showinfo("Ошибка", "Проверьте правильность введённых данных")
        else:
            global ways
            global directoryWay
            ways.append(directoryWay)
            ways.append(graphWay)
            ways.append(baseWay)
            choose_way.destroy()
            
    buttonOk = tki.Button(frameForDirectories, text = "Ок", command = checkWays)
    buttonOk.pack()
    choose_way.mainloop()
