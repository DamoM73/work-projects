import csv

class Student:
    def __init__(self, given_name, family_name, email):
        self.given_name = given_name
        self.family_name = family_name
        self.email = email
        self.activities = []

    def print_student(self):
        print(self.given_name, self.family_name, self.email, end=" ")
        for activity in self.activities:
            print(activity.name, activity.progress, end=" ")
        print("\n")
    
    def add_activity(self,name):
        self.activities.append(Activity(name))


class Subject:
    def __init__(self, name):
        self.name = name
        self.students = []
        
    def add_student(self,given_name, family_name, email):
        self.students.append(Student(given_name,family_name,email))

    def print_class(self):
        for student in self.students:
            student.print_student()

    def add_activity(self,name):
        for student in self.students:
            student.add_activity(name)

    def print_activities(self):
        for activity in self.students[0].activities:
            print(activity.name)

class Activity:
    def __init__(self,name):
        self.name = name
        self.progress = 0
        

def load_students(Subject):
    with open("students.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            Subject.add_student(row[0],row[1],row[2])

test = Subject("Test")
load_students(test)
test.add_activity("Test A")
test.print_class()
test.print_activities()