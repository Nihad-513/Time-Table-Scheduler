faculties = {}
subjects3 = {}
subjects5 = {}
fac = []
sub3 = []
# sub3 = ['ITT201','ITT203','ITT205','ITT207','EST200','MCN202','MAT303']
sub5 = []


def updatefac(obj):
        faculties[obj.Id]=obj
        fac.append(obj.Id)
        print(faculties)
        print(fac)

def updatesubj(semester,obj):
    if semester=='S3':
        subjects3[obj.code]=obj
        sub3.append(obj.code)
        print(sub3)
        print(subjects3)
    else:
        subjects5[obj.code]=obj
        sub5.append(obj.code)
        print(sub5)
        print(subjects5)

class Subject:
    def __init__(self ,n, c, f, m, s):
        self.name = n
        self.code = c
        self.faculty = f
        self.maxHour = m
        updatesubj(s,self)

    def getName(self): return self.name

    def getFaculty(self): return self.faculty

    def getMaxHour(self): return self.maxHour

class Faculty:
    def __init__(self, n, id, dep):
        self.name = n
        self.Id = id
        self.dept = dep
        updatefac(self)
    
    def getName(self): return  self.name 

    def getId(self): return self.Id