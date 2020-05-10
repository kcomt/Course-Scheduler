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
        N = 6
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

            for i in range(len(self.courses)):
                #get random number for day
                day = random.randint(0,4)
                #get random number for hour
                hour = random.randint(0,16-self.courses[i].duration)

                newState[hour][day].append(self.courses[i].courseName)
                newStateOjects[hour][day].append(self.courses[i])
            self.states.append(newState)
            self.statesObject.append(newStateOjects)

    def printPopulation(self):
        for i in self.states:
            print("\nState: ")
            for j in i:
                print(j)

class geneticAlgorithm:

    def __init__(self):
        self.mutation = 0.05

    #returns a value based on its fitness
    def idonityFunction(self,state):
        #Courses that intersect and have profesor or grade will rest most points
        #Rows are basically the time slots from 7 to 23
        totalPoints = 0
        contRow = 0
        for row in state:
            #Courses are the courses that start at that time slot, they from left to right so monday to friday
            contCourse = 0
            for courses in row:
                #Comparing courses that start in same timeslot
                for i in range(len(courses)):
                    for j in range(i,len(courses)):
                        #Compare if not the same object or course (seccion and course name)
                        if courses[i] != courses[j]:
                            #Compare if the same grade, if so rest some points
                            if courses[i].grade == courses[j].grade:
                                totalPoints -= 10000
                                
                            #Compare if the same profesor, if so rest some points
                            if courses[i].profesor == courses[j].profesor:
                                totalPoints -= 20000

                #Compairing future coures that start during the duration
                    for j in range(courses[i].duration):
                        for k in range(len(state[contRow+j][contCourse])):
                            #Compare if not the same object or course (seccion and course name)
                            if courses[i] != state[contRow+j][contCourse][k]:
                                #Compare if the same grade, if so rest some points
                                if courses[i].grade == state[contRow+j][contCourse][k].grade:
                                    totalPoints -= 10000
                                    
                                #Compare if the same profesor, if so rest some points
                                if courses[i].profesor == state[contRow+j][contCourse][k].profesor:
                                    totalPoints -= 20000     
                contCourse += 1                       
            contRow += 1

        #Check to see how many gaps are there in a given day and grade
        for grades in range(1,11):
            coursesEvaluated = []
            for days in range(5):
                timeIndex = []
                for hours in range(17):
                    if len(state[hours][days]) > 0:
                        if state[hours][days][0].grade == grades and state[hours][days][0] not in coursesEvaluated:
                            coursesEvaluated.append(state[hours][days][0])
                            aux = hours + (state[hours][days][0].duration-1)
                            timeIndex.append(aux)
                
                for i in range(0,len(timeIndex)-1):
                    aux = timeIndex[i+1] - timeIndex[i] - 1
                    totalPoints = totalPoints - aux*100
                
        return totalPoints
    
    #Finds best 2 to form a new offspring
    def findBest2OfPopulation(self,population):
        fitnessTotal = 0
        for i in range(len(population)):
            fitnessTotal += self.idonityFunction(population[i])

        percentage = []
        for i in range(len(population)):
            percentage.append(self.idonityFunction(population[i])/fitnessTotal)

        print(percentage)
        
populationObj = population()
geneticObj = geneticAlgorithm()

populationObj.addCourses()
populationObj.createPopulation()
populationObj.printPopulation()

geneticObj.findBest2OfPopulation(populationObj.statesObject)

