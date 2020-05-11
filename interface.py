import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import main as m
import courseClasses as c

inserted = False
number = 1

controllerObj = m.controller()
master = tk.Tk()
master.title("kc++")

width = 600
length = 600 
master.geometry(str(width)+"x"+str(length))

title = tk.Label(master, text = "Scheduler using Genetic Algorithms",font="Calibri 15", bg="light blue")
title.pack(pady = 20, fill=tk.BOTH, expand = True)

tabControl = ttk.Notebook(master)
tabControl.pack()

tab1 = ttk.Frame(tabControl,width=width,height=length)
tab2 = ttk.Frame(tabControl,width=width,height=length)
tab3 = ttk.Frame(tabControl,width=width,height=length)

tabControl.add(tab1, text="Add Course")
tabControl.add(tab2, text="See Courses")
tabControl.add(tab3, text="Generate Schedule/Info")

#Tab Add Course
label1 = tk.Label(tab1, text="Course Name: ", font="Calibri 10")
label1.pack(anchor="w",pady = 10,padx = 20)
textBoxCourseName = tk.Entry(tab1,font="Calibri 10")
textBoxCourseName.pack(anchor="w",pady = 10,padx = 20)

label2 = tk.Label(tab1, text="Seccion: ", font="Calibri 10")
label2.pack(anchor="w",pady = 10,padx = 20)
textBoxSeccions = tk.Entry(tab1,font="Calibri 10")
textBoxSeccions.pack(anchor="w",pady = 10,padx = 20)

label3 = tk.Label(tab1, text="Grade: ", font="Calibri 10")
label3.pack(anchor="w",pady = 10,padx = 20)
textBoxGrade = tk.Entry(tab1,font="Calibri 10")
textBoxGrade.pack(anchor="w",pady = 10,padx = 20)

label4 = tk.Label(tab1, text="Professor: ", font="Calibri 10")
label4.pack(anchor="w",pady = 10,padx = 20)
textBoxProfessor = tk.Entry(tab1,font="Calibri 10")
textBoxProfessor.pack(anchor="w",pady = 10,padx = 20)

label5 = tk.Label(tab1, text="Duration: ", font="Calibri 10")
label5.pack(anchor="w",pady = 10,padx = 20)
textBoxDuration = tk.Entry(tab1,font="Calibri 10")
textBoxDuration.pack(anchor="w",pady = 10,padx = 20)

def saveCourse():
    courseName = textBoxCourseName.get()
    seccions = textBoxSeccions.get()
    grade = int(textBoxGrade.get())
    profesor = textBoxProfessor.get()
    duration = int(textBoxDuration.get())

    auxSeccion = c.course(0,courseName,seccions,grade,profesor,duration)
    controllerObj.addCourse(auxSeccion)
    listBox.insert(tk.END,str(number) + ". Curso:  " + courseName +"   Seccion: " +seccions + "     Ciclo: "+ str(grade) +"  Profesor:  " + 
    profesor + "    Duration:  " + str(duration))

    textBoxCourseName.delete(0,tk.END)
    textBoxSeccions.delete(0,tk.END)
    textBoxGrade.delete(0,tk.END)
    textBoxProfessor.delete(0,tk.END)
    textBoxDuration.delete(0,tk.END)
    number += 1
    messagebox.showinfo(title="Exito", message="Se guardo exitosamente el curso!")

def deleteAll():
    controllerObj.deleteAll()
    listBox.delete(0,tk.END)
    messagebox.showinfo(title="Exito", message="Se borraron todo los cursos!")
    print(len(controllerObj.populationObj.courses))
buttonAdd = tk.Button(tab1, text = "Add Course", command = saveCourse)
buttonAdd.pack(pady = 10,padx = 20)

#Tab 2
buttonDelete= tk.Button(tab2, text = "Delete All Courses", command = deleteAll)
buttonDelete.pack(pady = 10,padx = 20)

listBox = tk.Listbox(tab2,height=400,width=300, font="Calibri 12")
listBox.pack(padx = 10, pady = 10)
if not inserted:
    for i in range(len(controllerObj.populationObj.courses)):
        listBox.insert(tk.END,str(number) + ". Curso:  " + controllerObj.populationObj.courses[i].courseName +"   Seccion: " +controllerObj.populationObj.courses[i].seccion  + 
        "     Ciclo: "+ str(controllerObj.populationObj.courses[i].grade) +"  Profesor:  " + controllerObj.populationObj.courses[i].profesor +
         "    Duration:  " + str(controllerObj.populationObj.courses[i].duration))
        number += 1
    insert = True

#Tab 3
def generate():
    controllerObj.runAlgorithm()
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

    window = tk.Toplevel(master,bg="light blue")
    window.title("Ciclo 1")
    
    for i in range(17):
        label = tk.Label(window, text=str(i+7)+":00 Horas",bg="light blue")
        label.grid(row = 1+i, column = 0)

    for i in range(len(days)):
        label = tk.Label(window, text=days[i],bg="light blue")
        label.grid(row = 0, column = i+1)

    ciclo1 = controllerObj.returnScheduleBasedOnGrade(1)
    for i in range(17):
        for j in range(5):
            if len(ciclo1[i][j]) > 0:
                label = tk.Label(window, text=str(ciclo1[i][j][0]),bg="light blue")
                label.grid(row = i+1, column = j+1 )
            else:
                label = tk.Label(window, text="Vacio",bg="light blue")
                label.grid(row = i+1, column = j+1 )  

    window2 = tk.Toplevel(master,bg="light pink")
    window2.title("Ciclo 2")
    
    for i in range(17):
        label = tk.Label(window2, text=str(i+7)+":00 Horas",bg="light pink")
        label.grid(row = 1+i, column = 0)

    for i in range(len(days)):
        label = tk.Label(window2, text=days[i],bg="light pink")
        label.grid(row = 0, column = i+1)

    ciclo1 = controllerObj.returnScheduleBasedOnGrade(2)
    for i in range(17):
        for j in range(5):
            if len(ciclo1[i][j]) > 0:
                label = tk.Label(window2, text=str(ciclo1[i][j][0]),bg="light pink")
                label.grid(row = i+1, column = j+1 )
            else:
                label = tk.Label(window2, text="Vacio",bg="light pink")
                label.grid(row = i+1, column = j+1 )  

    window3 = tk.Toplevel(master,bg="orange")
    window3.title("Ciclo 3")
    
    for i in range(17):
        label = tk.Label(window3, text=str(i+7)+":00 Horas",bg="orange")
        label.grid(row = 1+i, column = 0)

    for i in range(len(days)):
        label = tk.Label(window3, text=days[i],bg="orange")
        label.grid(row = 0, column = i+1)

    ciclo1 = controllerObj.returnScheduleBasedOnGrade(3)
    for i in range(17):
        for j in range(5):
            if len(ciclo1[i][j]) > 0:
                label = tk.Label(window3, text=str(ciclo1[i][j][0]),bg="orange")
                label.grid(row = i+1, column = j+1 )
            else:
                label = tk.Label(window3, text="Vacio",bg="orange")
                label.grid(row = i+1, column = j+1 )  
    

    window4 = tk.Toplevel(master,bg="brown")
    window4.title("Ciclo 4")
    
    for i in range(17):
        label = tk.Label(window4, text=str(i+7)+":00 Horas",bg="brown")
        label.grid(row = 1+i, column = 0)

    for i in range(len(days)):
        label = tk.Label(window4, text=days[i],bg="brown")
        label.grid(row = 0, column = i+1)

    ciclo1 = controllerObj.returnScheduleBasedOnGrade(4)
    for i in range(17):
        for j in range(5):
            if len(ciclo1[i][j]) > 0:
                label = tk.Label(window4, text=str(ciclo1[i][j][0]),bg="brown")
                label.grid(row = i+1, column = j+1 )
            else:
                label = tk.Label(window4, text="Vacio",bg="brown")
                label.grid(row = i+1, column = j+1 )  

    window5 = tk.Toplevel(master,bg="light yellow")
    window5.title("Ciclo 5")
    
    for i in range(17):
        label = tk.Label(window5, text=str(i+7)+":00 Horas",bg="light yellow")
        label.grid(row = 1+i, column = 0)

    for i in range(len(days)):
        label = tk.Label(window5, text=days[i],bg="light yellow")
        label.grid(row = 0, column = i+1)

    ciclo1 = controllerObj.returnScheduleBasedOnGrade(5)
    for i in range(17):
        for j in range(5):
            if len(ciclo1[i][j]) > 0:
                label = tk.Label(window5, text=str(ciclo1[i][j][0]),bg="light yellow")
                label.grid(row = i+1, column = j+1 )
            else:
                label = tk.Label(window5, text="Vacio",bg="light yellow")
                label.grid(row = i+1, column = j+1 )

    window6 = tk.Toplevel(master,bg="red")
    window6.title("Ciclo 6")
    
    for i in range(17):
        label = tk.Label(window6, text=str(i+7)+":00 Horas",bg="red")
        label.grid(row = 1+i, column = 0)

    for i in range(len(days)):
        label = tk.Label(window6, text=days[i],bg="red")
        label.grid(row = 0, column = i+1)

    ciclo1 = controllerObj.returnScheduleBasedOnGrade(6)
    for i in range(17):
        for j in range(5):
            if len(ciclo1[i][j]) > 0:
                label = tk.Label(window6, text=str(ciclo1[i][j][0]),bg="red")
                label.grid(row = i+1, column = j+1 )
            else:
                label = tk.Label(window6, text="Vacio",bg="red")
                label.grid(row = i+1, column = j+1 )

    window7 = tk.Toplevel(master,bg="light green")
    window7.title("Ciclo 7")
    
    for i in range(17):
        label = tk.Label(window7, text=str(i+7)+":00 Horas",bg="light green")
        label.grid(row = 1+i, column = 0)

    for i in range(len(days)):
        label = tk.Label(window7, text=days[i],bg="light green")
        label.grid(row = 0, column = i+1)

    ciclo1 = controllerObj.returnScheduleBasedOnGrade(7)
    for i in range(17):
        for j in range(5):
            if len(ciclo1[i][j]) > 0:
                label = tk.Label(window7, text=str(ciclo1[i][j][0]),bg="light green")
                label.grid(row = i+1, column = j+1 )
            else:
                label = tk.Label(window7, text="Vacio",bg="light green")
                label.grid(row = i+1, column = j+1 )

    window8 = tk.Toplevel(master,bg="blue")
    window8.title("Ciclo 8")
    
    for i in range(17):
        label = tk.Label(window8, text=str(i+7)+":00 Horas",bg="blue")
        label.grid(row = 1+i, column = 0)

    for i in range(len(days)):
        label = tk.Label(window8, text=days[i],bg="blue")
        label.grid(row = 0, column = i+1)

    ciclo1 = controllerObj.returnScheduleBasedOnGrade(8)
    for i in range(17):
        for j in range(5):
            if len(ciclo1[i][j]) > 0:
                label = tk.Label(window8, text=str(ciclo1[i][j][0]),bg="blue")
                label.grid(row = i+1, column = j+1 )
            else:
                label = tk.Label(window8, text="Vacio",bg="blue")
                label.grid(row = i+1, column = j+1 )

    window9 = tk.Toplevel(master,bg="yellow")
    window9.title("Ciclo 9")
    
    for i in range(17):
        label = tk.Label(window9, text=str(i+7)+":00 Horas",bg="yellow")
        label.grid(row = 1+i, column = 0)

    for i in range(len(days)):
        label = tk.Label(window9, text=days[i],bg="yellow")
        label.grid(row = 0, column = i+1)

    ciclo1 = controllerObj.returnScheduleBasedOnGrade(9)
    for i in range(17):
        for j in range(5):
            if len(ciclo1[i][j]) > 0:
                label = tk.Label(window9, text=str(ciclo1[i][j][0]),bg="yellow")
                label.grid(row = i+1, column = j+1 )
            else:
                label = tk.Label(window9, text="Vacio",bg="yellow")
                label.grid(row = i+1, column = j+1 )

    window10 = tk.Toplevel(master,bg="green")
    window10.title("Ciclo 10")
    
    for i in range(17):
        label = tk.Label(window10, text=str(i+7)+":00 Horas",bg="green")
        label.grid(row = 1+i, column = 0)

    for i in range(len(days)):
        label = tk.Label(window10, text=days[i],bg="green")
        label.grid(row = 0, column = i+1)

    ciclo1 = controllerObj.returnScheduleBasedOnGrade(10)
    for i in range(17):
        for j in range(5):
            if len(ciclo1[i][j]) > 0:
                label = tk.Label(window10, text=str(ciclo1[i][j][0]),bg="green")
                label.grid(row = i+1, column = j+1 )
            else:
                label = tk.Label(window10, text="Vacio",bg="green")
                label.grid(row = i+1, column = j+1 )

buttonGenerate= tk.Button(tab3, text = "Generate Schedule", command = generate)
buttonGenerate.pack(pady = 10,padx = 20)

canvas = tk.Canvas(tab3,width=200,height=400)
canvas.pack()
canvas.create_text(100,180,text="This is scheduling program.")
canvas.create_text(100,200,text="It was made with Python")
canvas.create_text(100,220,text="using genetic algorithms.")
canvas.create_text(100,240,text="It's main objetive")
canvas.create_text(100,260,text="is to schedule")
canvas.create_text(100,280,text="courses of a given career,")
canvas.create_text(100,300,text="like Software Engineering.")
canvas.create_text(100,320,text="It tries to eliminate same grade ")
canvas.create_text(100,340,text="course and same profesor conflicts.")
canvas.create_text(100,360,text="It was made for a")
canvas.create_text(100,380,text="college project. Enjoy.")
master.mainloop()   