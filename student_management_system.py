#object vs instance
class StudentInfo:
    def __init__(self):
        self.NameInfo = ''
        self.personalID = ''
        self.departInfo = ''
        self.jobInfo = ''
        self.student = list()

    def getName(self):
        return self.NameInfo

    def setName(self, name):
        self.NameInfo = name

    def getID(self):
        return self.personalID

    def setID(self, id):
        self.personalID = id

    def getDepart(self):
        return self.departInfo

    def setDepart(self, depart):
        self.departInfo = depart

    def getJob(self):
        return self.jobInfo

    def setJob(self, job):
        self.jobInfo = job

    def addStudent(self, name, id, depart, job):
        self.student.append(self.NameInfo)
        self.student.append(self.personalID)
        self.student.append(self.departInfo)
        self.student.append(self.jobInfo)
        print('added')

    def searchStudent(self, name, id, depart, job):
        if name in self.student or id in self.student or depart in self.student or job in self.student:
            print("Student is present")
        else:
            print("no records found")

    def deleteStudent(self, name, id, depart, job):
        deleting_list = [name, id, depart, job]
        self.student.remove(deleting_list)
        print('deleted')


def main():
    name = str(input("Name:"))
    id = str(input("id:"))
    depart = str(input("depart:"))
    job = str(input("job:"))
    students = StudentInfo() #insatance of StudentInfo
    students.setName(name)
    students.setID(id)
    students.setDepart(depart)
    students.setJob(job)

    a = input("choice 1:add 2:delete 3:search 4:exit")

    if a == '1':
        students.addStudent(name, id, depart, job)
    elif a == '2':
        students.deleteStudent(name, id, depart, job)
    elif a == '3':
        students.searchStudent(name, id, depart, job)
    else:
        return #will continue the main method from where it left off

    try:
        with open("student.txt", "w") as file2: 
            #opening the file with w(overwrite if already exist or create a new one) and making an alias 
            print('opened file')
            for x in students.student: #students is an object and student is a list of class StudentInfo.
                file2.write(str(x) + "\n")
                print('successflly written in file')

    except IOError:
        print("The specified filename cannot be found or opened")
    except ValueError:
        print("A non-integer value is given as a line number")
    except IndexError:
        print("The line number is outside the range of the data list.")

if (__name__ == '__main__'): # used to execute some code only if the file was run directly, and not imported
 main()
