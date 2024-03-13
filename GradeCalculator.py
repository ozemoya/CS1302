type_grade = int(input("How many types of grades do you have? "))
total = []
weights = []

class GradeCalculator():
    def __init__(self):
        self.grades = []
        self.weight = 0
        self.final_grade = 0

    def add_grade(self):
        self.amount = int(input("How many Assignments for the grade type " + str(x+1) + " do you have? "))
        for i in range(self.amount):
            new_grade = float(input("What was your grade for assignment " + str(i+1) + "? "))
            self.grades.append(new_grade)

       
        self.weight = self.add_percentage()

    def add_percentage(self):
        grade_p = float(input("What is the weight of the grade (decimals)? "))
        weights.append(grade_p)
        return grade_p

    def calculate_final_grade(self):
        if self.amount == 0:
            return 0  
        total_scores = sum(self.grades) / self.amount
        self.final_grade = total_scores * self.weight
        return self.final_grade


for x in range(type_grade):
    grade_calculator_initializer = GradeCalculator()
    grade_calculator_initializer.add_grade()
    total.append(grade_calculator_initializer.calculate_final_grade())

# Calculate the overall final grade
final_grade = sum(total) / sum(weights)

print(f"Your overall final grade is {final_grade:.2f}")

if final_grade < 60:
    print("F")
elif 60 <= final_grade <= 69:
    print("D")
elif 70 <= final_grade <= 76:
    print("C")
elif 76 <= final_grade <= 79:
    print("C+")
elif 80 <= final_grade <= 82:
    print("B-")
elif 83 <= final_grade <= 86:
    print("B")
elif 87 <= final_grade <= 89:
    print("B+")
elif 90 <= final_grade <= 92:
    print("A-")
elif 93 <= final_grade <= 96:
    print("A")
elif 97 <= final_grade <= 100:
    print("A+")
else:
    print("A+")
type_grade = int(input("How many types of grades do you have? "))
total = []
weights = []

class GradeCalculator():
    def __init__(self):
        self.grades = []
        self.weight = 0
        self.final_grade = 0

    def add_grade(self):
        self.amount = int(input("How many Assignments for the grade type " + str(x+1) + " do you have? "))
        for i in range(self.amount):
            new_grade = float(input("What was your grade for assignment " + str(i+1) + "? "))
            self.grades.append(new_grade)

       
        self.weight = self.add_percentage()

    def add_percentage(self):
        grade_p = float(input("What is the weight of the grade (decimals)? "))
        weights.append(grade_p)
        return grade_p

    def calculate_final_grade(self):
        if self.amount == 0:
            return 0  
        total_scores = sum(self.grades) / self.amount
        self.final_grade = total_scores * self.weight
        return self.final_grade


for x in range(type_grade):
    grade_calculator_initializer = GradeCalculator()
    grade_calculator_initializer.add_grade()
    total.append(grade_calculator_initializer.calculate_final_grade())

# Calculate the overall final grade
final_grade = sum(total) / sum(weights)

print(f"Your overall final grade is {final_grade:.2f}")

if final_grade < 60:
    print("F")
elif 60 <= final_grade <= 69:
    print("D")
elif 70 <= final_grade <= 76:
    print("C")
elif 76 <= final_grade <= 79:
    print("C+")
elif 80 <= final_grade <= 82:
    print("B-")
elif 83 <= final_grade <= 86:
    print("B")
elif 87 <= final_grade <= 89:
    print("B+")
elif 90 <= final_grade <= 92:
    print("A-")
elif 93 <= final_grade <= 96:
    print("A")
elif 97 <= final_grade <= 100:
    print("A+")
else:
    print("A+")