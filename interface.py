import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import main as m
import courseClasses as c

inserted = False

controllerObj = m.controller()
master = tk.Tk()

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
tabControl.add(tab3, text="Generate Schedule")

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
    listBox.insert(tk.END," Curso:  " + courseName +"   Seccion: " +seccions + "     Ciclo: "+ str(grade) +"  Profesor:  " + 
    profesor + "    Duration:  " + str(duration))

    textBoxCourseName.delete(0,tk.END)
    textBoxSeccions.delete(0,tk.END)
    textBoxGrade.delete(0,tk.END)
    textBoxProfessor.delete(0,tk.END)
    textBoxDuration.delete(0,tk.END)

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
        listBox.insert(tk.END," Curso:  " + controllerObj.populationObj.courses[i].courseName +"   Seccion: " +controllerObj.populationObj.courses[i].seccion  + 
        "     Ciclo: "+ str(controllerObj.populationObj.courses[i].grade) +"  Profesor:  " + controllerObj.populationObj.courses[i].profesor +
         "    Duration:  " + str(controllerObj.populationObj.courses[i].duration))
    insert = True

#Tab 3
buttonGenerate= tk.Button(tab3, text = "Generate Schedule", command = deleteAll)
buttonGenerate.pack(pady = 10,padx = 20)

master.mainloop()