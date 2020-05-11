import random
random.seed()

class course:
    def __init__(self,courseId,courseName,seccion,grade,profesor,duration):
        self.courseId = courseId
        self.courseName = courseName
        self.seccion = seccion
        self.grade = grade
        self.profesor = profesor
        self.duration = duration

class population:    
    timeTable =[
        [[],[],[],[],[],[]],#7:00
        [[],[],[],[],[],[]],#8:00
        [[],[],[],[],[],[]],#9:00
        [[],[],[],[],[],[]],#10:00
        [[],[],[],[],[],[]],#11:00
        [[],[],[],[],[],[]],#12:00
        [[],[],[],[],[],[]],#13:00
        [[],[],[],[],[],[]],#14:00
        [[],[],[],[],[],[]],#15:00
        [[],[],[],[],[],[]],#16:00
        [[],[],[],[],[],[]],#17:00
        [[],[],[],[],[],[]],#18:00
        [[],[],[],[],[],[]],#19:00
        [[],[],[],[],[],[]],#20:00
        [[],[],[],[],[],[]],#21:00
        [[],[],[],[],[],[]],#22:00
        [[],[],[],[],[],[]]#23:00
        ]
        #L,M,M,J,V

    timeTableObjects =[
        [[],[],[],[],[],[]],#7:00
        [[],[],[],[],[],[]],#8:00
        [[],[],[],[],[],[]],#9:00
        [[],[],[],[],[],[]],#10:00
        [[],[],[],[],[],[]],#11:00
        [[],[],[],[],[],[]],#12:00
        [[],[],[],[],[],[]],#13:00
        [[],[],[],[],[],[]],#14:00
        [[],[],[],[],[],[]],#15:00
        [[],[],[],[],[],[]],#16:00
        [[],[],[],[],[],[]],#17:00
        [[],[],[],[],[],[]],#18:00
        [[],[],[],[],[],[]],#19:00
        [[],[],[],[],[],[]],#20:00
        [[],[],[],[],[],[]],#21:00
        [[],[],[],[],[],[]],#22:00
        [[],[],[],[],[],[]]#23:00
        ]
        #L,M,M,J,V

    def __init__(self):
        self.courses = []
        self.states = []
        self.statesObject = []
    
    #This is for testing, before the GUI
    def initializeCourses(self):
        #ciclo1
        course1 = course("MA1","Math 1","1",1,"Juan Silva",2)
        course2 = course("MA1","Math 1","2",1,"Williy Enrique",2)

        course2 = course("PG1","Programacion 1","1",1,"Williy Enrique",3)
        course3 = course("PG1","Programacion 1","2",1,"Williy Enrique",3)
    
        course4 = course("LE1","English 1","1",1,"Daniel Diaz",2)
        course5 = course("LE1","English 1","2",1,"Luis Kcomt",2)

        course6 = course("CH1","Chemisty 1","1",1,"Miguel Andres",2)
        course7 = course("CH1","Chemisty 1","2",1,"Miguel Andres",2)

        #ciclo2
        course8 = course("CH1","Chemisty 2","1",2,"Miguel Andres",2)
        course9 = course("CH1","Chemisty 2","2",2,"Ricardo Guevara",2)

        course10 = course("PG1","Programacion 2","1",2,"Jaily Arteaga",3)
        course11 = course("PG1","Programacion 2","2",2,"Jaily Arteaga",3)

        course12 = course("PG1","Calculo","1",2,"Santiago Lopez",4)
        course13 = course("PG1","Calculo","2",2,"Juan Silva",4)
        course14 = course("PG1","Calculo","3",2,"Santiago Lopez",4)
        course15 = course("PG1","Calculo","4",2,"Williy Enrique",4)

        course16 = course("PG1","Mate Discreta","1",2,"Willy Enrique",3)
        course17 = course("PG1","Mate Discreta","2",2,"Bruno Atocha",3)

        #ciclo3
        course18 = course("CH1","Algoritmos","1",3,"Luis Kcomt",2)
        course19 = course("CH1","Algoritmos","2",3,"Wans",2)
        course20 = course("CH1","Algoritmos","3",3,"Wans",2)

        course21 = course("PG1","Base de datos","1",3,"Carlos Larios",3)
        course22 = course("PG1","Base de datos","2",3,"Ricardo Guevara",3)

        course23 = course("PG1","Calculo 2","1",3,"Santiago Lopez",3)
        course24 = course("PG1","Calculo 2","2",3,"Carlos Larios",3)

        course25 = course("PG1","Requerimientos","1",3,"Carlos Larios",3)
        course26 = course("PG1","Requerimientos","2",3,"Guillermo Lam",3)
        
        self.courses.append(course1)
        self.courses.append(course2)
        self.courses.append(course3)
        self.courses.append(course4)
        self.courses.append(course5)
        self.courses.append(course6)
        self.courses.append(course7)
        self.courses.append(course8)
        self.courses.append(course9)
        self.courses.append(course10)
        self.courses.append(course11)
        self.courses.append(course12)
        self.courses.append(course13)
        self.courses.append(course14)
        self.courses.append(course15)
        self.courses.append(course16)
        self.courses.append(course17)
        self.courses.append(course18)
        self.courses.append(course19)
        self.courses.append(course20)
        self.courses.append(course21)
        self.courses.append(course22)
        self.courses.append(course23)
        self.courses.append(course24)
        self.courses.append(course25)
        self.courses.append(course26)
    def addCourse(self,coursep):
        self.courses.append(coursep)
        
    def createPopulation(self):
        N = 10
        for n in range(N):
            #fresh state to insert in to population
            newState = []
            newStateOjects = []

            for i in self.timeTable:
                line = []
                for j in i:
                    line.append(j.copy())
                newState.append(line)

            for i in self.timeTableObjects:
                line = []
                for j in i:
                    line.append(j.copy())
                newStateOjects.append(line)

            day = 0
            for i in range(len(self.courses)):
                #get random number for hour
                hour = random.randint(0,15-self.courses[i].duration)
                newState[hour][day].append(self.courses[i].courseName)
                newStateOjects[hour][day].append(self.courses[i])
                if day >= 4:
                    day = 0
                day = day + 1
            self.states.append(newState)
            self.statesObject.append(newStateOjects)

    def printPopulation(self):
        for i in self.states:
            print("\nState: ")
            for j in i:
                print(j)

