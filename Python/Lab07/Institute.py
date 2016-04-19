import re
class Simulation:
    def __init__(self, number, date, name, count, cost):
        self.simulationNumber = number
        self.simulationDate = date
        self.chipName = name
        self.chipCount = count
        self.chipCost = cost
        self.simulationCost = count * cost

    def __str__(self):
        simcost = "{:.2f}".format(self.simulationCost)
        return "{}: {:0=03d}, {}, ${}".format(self.chipName,self.simulationNumber,self.simulationDate,str.zfill(simcost,6))

class Employee:
    def __init__(self, name, eid):
        self.employeeName = name
        self.employeeID = eid
        self.simulationsDict = {}

    def __str__(self):
        num = len(self.simulationsDict)
        return "{}, {}: {} Simulations".format(self.employeeID, self.employeeName, str.zfill(str(num),2))

    def addSimulation(self, sim):
        self.simulationsDict[sim.simulationNumber] = sim

    def getSimulation(self, number):
        if number in self.simulationsDict.keys():
            return self.simulationsDict[number]
        return None

    def getWorkload(self):
        load = self.__str__()
        lst = []
        for sim in self.simulationsDict.values():
            lst.append(str(sim))
        lst.sort()
        for it in lst:
            load += "\n" + it
        return load

    def addWorkload(self, file):
        r1 = re.compile(r"^(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+\$(\S+)\n$")
        with open(file, 'r') as myfile:
            content = myfile.readlines()
        for i in range(2, len(content)):
            l = r1.match(content[i])
            sim = Simulation(int(l.group(1)), l.group(2), l.group(3), int(l.group(4)), float(l.group(5)))
            self.addSimulation(sim)


class Facility:
    def __init__(self, name):
        self.facilityName = name
        self.employeesDict = {}

    def __str__(self):
        num = len(self.employeesDict)
        fac_str = "{}: {} Employees".format(self.facilityName, str.zfill(str(num),2))
        lst = []
        for work in self.employeesDict.values():
            lst.append(str(work))
        lst.sort()
        for it in lst:
            fac_str += "\n" + it
        return fac_str

    def addEmployee(self, e):
        self.employeesDict[e.employeeName] = e

    def getEmployees(self, *args):
        lst = []
        for name in args:
            if name in self.employeesDict.keys():
                lst.append(self.employeesDict[name])
        return lst

    def getSimulation(self, number):
        for e in self.employeesDict.values():
            if number in e.simulationsDict.keys():
                return e.simulationsDict[number]
        return None





