import statistics

class Student:
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def get_grade(self):
        return self._grade
    
def basic_stats(list_of_student_objects):
    grades = [student.get_grade() for student in list_of_student_objects]
    # for student in list_of_student_objects:
    #     grades.append(student.get_grade()) 
    mean =  statistics.mean(grades)
    median = statistics.median(grades)
    mode = statistics.mode(grades)

    answer = (mean, median, mode)
    return answer

s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

student_list =[s1, s2, s3, s4]
print(basic_stats(student_list)) 