import courseClasses as c
import random
random.seed()
class geneticAlgorithm:

    def __init__(self):
        self.mutation = 0.05

    #returns a value based on its fitness
    def idonityFunction(self,state,Totalcourses):
        #Courses that intersect and have profesor or grade will rest most points
        #Rows are basically the time slots from 7 to 23
        totalPoints = 0
        contRow = 0
        couresInSchedule = []

        for row in state:
            #Courses are the courses that start at that time slot, they from left to right so monday to friday
            contCourse = 0
            for courses in row:
                #Comparing courses that start in same timeslot
                for i in range(len(courses)):
                    for j in range(i,len(courses)):

                        if courses[j] not in couresInSchedule:
                            couresInSchedule.append(courses[j])

                        #Compare if not the same object or course (seccion and course name)
                        if courses[i] != courses[j]:
                            #Compare if the same grade, if so rest some points
                            if courses[i].grade == courses[j].grade:
                                totalPoints -= 20000
                                
                            #Compare if the same profesor, if so rest some points
                            if courses[i].profesor == courses[j].profesor:
                                totalPoints -= 30000

                #Compairing future coures that start during the duration
                    for j in range(courses[i].duration):
                        for k in range(len(state[contRow+j][contCourse])):
                            #Compare if not the same object or course (seccion and course name)
                            if courses[i] != state[contRow+j][contCourse][k]:
                                #Compare if the same grade, if so rest some points
                                if courses[i].grade == state[contRow+j][contCourse][k].grade:
                                    totalPoints -= 20000
                                    
                                #Compare if the same profesor, if so rest some points
                                if courses[i].profesor == state[contRow+j][contCourse][k].profesor:
                                    totalPoints -= 30000     
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
        
        if len(Totalcourses) == len(couresInSchedule):
            return totalPoints
        else:
            return -500000
    
    #Finds best 2 to 5 times to form 2 new offspring and population
    def findBestOfPopulation(self,population,courses):
        fitness = []
        percentage = []

        for i in range(len(population)):
            fitness.append(self.idonityFunction(population[i],courses))
            percentage.append(0)
        
        #Best state has 23% to be chosen, the next 20, and so on. Last 2 have 0% of being chosen
        for i in range(1,9):
            index = fitness.index(max(fitness))
            percentage[index] = 26-i*3
            fitness[index] = -1000000
        
        #Going to pick out 2 states from possibility array, which represents each state of current population chance of getting picked
        possibility = []
        for i in range(len(percentage)):
           for j in range(percentage[i]):
               possibility.append(population[i])
        
        #Going to pick 2 parents 5 times, and form 2 offspring from that
        newPopulation = []
        for i in range(5):
            indexParent1 = random.randint(0,99)
            indexParent2 = random.randint(0,99)
            newPopulation.append(self.merge(possibility[indexParent1],possibility[indexParent2]))
        
        return newPopulation

    def merge(self,parent1,parent2):
        son =[
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

        #Cross will be horizontal
        randomIndex = random.randint(0,4)
        for i in range(0,len(parent1)):
            for j in range(0,randomIndex):
                son[i][j] = parent1[i][j].copy()

        for i in range(0,len(parent2)):
            for j in range(randomIndex,5):
                son[i][j] = parent2[i][j].copy()
        
        #random mutation
        if random.randint(0,99) < self.mutation*100:
            randomDay = random.randint(0,4)
            randomHour = random.randint(0,13)
            randomHour2 = random.randint(0,13)

            aux = son[randomHour][randomDay].copy()
            son[randomHour][randomDay] = son[randomHour2][randomDay].copy()
            son[randomHour2][randomDay] = aux.copy()
        return son

class controller:
    def __init__(self):
        self.populationObj = c.population()
        self.geneticObj = geneticAlgorithm()
        self.populationObj.initializeCourses()
        self.populationObj.createPopulation()
        self.population = self.populationObj.statesObject
        self.finalSolution = []

    def runAlgorithm(self):
        solutionFound = False
        while not solutionFound:
            #get new population based on old
            population = self.geneticObj.findBestOfPopulation(self.population, self.populationObj.courses)
            #get fitness of new population
            fitness = []
            for i in population:
                fitness.append(self.geneticObj.idonityFunction(i,self.populationObj.courses))
            
            if max(fitness) >= -45000:
                print("Solution found or aprox")
                solutionFound = True
                indexMax = fitness.index(max(fitness))
                scheduleFinal = population[indexMax]
            else:
                print(max(fitness))
        self.finalSolution = scheduleFinal

    def addCourse(self,course):
        self.populationObj.addCourse(course)
    
    def deleteAll(self):
        self.populationObj.courses = []
    
    def getCourses():
        return self.populationObj.coures

    def returnScheduleBasedOnGrade(self,grade):
        scheduleFinalForGrade =[
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

        for row in range(len(self.finalSolution)):
            for column in range(len(self.finalSolution[row])):
                for i in range(len(self.finalSolution[row][column])):
                    if self.finalSolution[row][column][i].grade == grade:
                        for j in range(self.finalSolution[row][column][i].duration):
                            scheduleFinalForGrade[row+j][column].append(self.finalSolution[row][column][i].courseName + " con "+
                            self.finalSolution[row][column][i].profesor)

        return scheduleFinalForGrade