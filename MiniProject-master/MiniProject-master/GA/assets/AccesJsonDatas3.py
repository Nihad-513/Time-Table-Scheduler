import json
import assets.Attributes as att

def addfaculty(faculties):
    if len(faculties) == 0:
        return "No faculties provided"
    else:
        with open("facultiess1.json",'a') as f:
            for i in faculties:
                json_str = json.dump(faculties[i].__dict__)
                f.write("\n"+json_str)
        return "Faculties added successfully!"

def addsubject():
    if len(att.subjects3)== 0:
        return "No subjects provided"
    else:
        with  open('subjectss1.json', 'a') as s:
            for i in att.subjects3:
                json_str = json.dump(att.subjects3[i].__dict__)
                s.write("\n"+json_str)
        return "Subjects added successfully!"

def getfaculty():
    with open("facultiess1.json",'r') as f:
        for i in f:
            jsonstr = json.loads(i)
            obj = att.Faculty(jsonstr['name'],jsonstr['Id'])
            att.Faculty.updatefac(obj)
        return "Faculties Fetched!"

def getsubjects():
    with open("subjectss1.json",'r') as f:
        for i in f:
            jsonstr = json.loads(i)
            obj = att.Subject(jsonstr['name'],jsonstr['code'],jsonstr["faculty"],jsonstr["maxHour"])
            att.Subject.updateSub(obj)
        return "Subjects Fetched!"