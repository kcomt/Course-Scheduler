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
        [["x"],[],[],[],[],["x"]],#11:00
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

    def addCourses(self):
        course1 = course("MA1","Math 1","1",1,"Juan Manuel",2)
        course2 = course("MA1","Math 1","2",1,"Williy Enrique",2)

        course2 = course("PG1","Programacion 1","1",1,"Williy Enrique",3)
        course3 = course("PG1","Programacion 1","2",1,"Juan Manuel",3)

        course4 = course("LE1","English 1","1",1,"Kim Yung",2)
        course5 = course("LE1","English 1","2",1,"Kim Yung",2)

        course6 = course("CH1","Chemisty 1","1",1,"BOR BOR",2)
        course7 = course("CH1","Chemisty 1","2",1,"BOR BOR",2)

        self.courses.append(course1)
        self.courses.append(course2)
        self.courses.append(course3)
        self.courses.append(course4)
        self.courses.append(course5)
        self.courses.append(course6)
        self.courses.append(course7)

    def createPopulation(self):
        N = 3
        for n in range(N):
            #fresh state to insert in to population
            newState = []
            for i in self.timeTable:
                line = []
                for j in i:
                    line.append(j.copy())
                newState.append(line)

            for i in range(len(self.courses)):
                #get random number for day
                day = random.randint(0,4)
                #get random number for hour
                hour = random.randint(0,16)

                newState[hour][day].append(self.courses[i].courseName)
            
            self.states.append(newState)
    
    def printPopulation(self):
        for i in self.states:
            print("\nState: ")
            for j in i:
                print(j)

populationObj = population()
populationObj.addCourses()
populationObj.createPopulation()
populationObj.printPopulation()