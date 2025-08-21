import json
import assets.Attributes as att

def addsubject():
    if len(att.subjects5)== 0:
        return "No subjects provided"
    else:
        with  open('subjectss5.json', 'a') as s:
            for i in att.subjects5:
                json_str = json.dump(att.subjects5[i].__dict__)
                s.write("\n"+json_str)
        return "Subjects added successfully!"


def getsubjects():
    with open("subjectss5.json",'r') as f:
        for i in f:
            jsonstr = json.loads(i)
            obj = att.Subject(jsonstr['name'],jsonstr['code'],jsonstr["faculty"],jsonstr["maxHour"])
            att.subjects5[obj.Id]=obj
            att.sub5.append(obj.Id)
        return "Subjects Fetched!"