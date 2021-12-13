"""
First I have created a class with a constructor inside it with three parameters to be used through out the class.
When an object of the class is created it will have to contain the three arguments.
Next I have three basic functions:
1:The first 'def display_name' returns the first and last name entered.
2:The second function 'def display_email' returns the first and last name and adds '@yahoo.ie'.
  It then makes all the letters lowercase.
3:The third function 'def display_average_score' returns the average of the grades entered in the object of the class.
I then added the @property decorator on all the functions so the functions become properties of the class.
I can do this because each function only has one parameter 'self'.
Next I created an object of the class and stored it in student_one. I passed three arguments to it
and printed the various properties to the console just to make sure everything was working.
I have commented out this part and no deleted it so that anyone can quickly see that everything is working so far.
Now its over to the test_student_info.py file to carry out the testing.
"""


class StudentInfo:
    def __init__(self, first, last, grades):
        self.first_name = first
        self.last_name = last
        self.grades = grades

    @property
    def display_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def display_email(self):
        return f"{self.first_name}{self.last_name}@yahoo.ie".lower()

    @property
    def display_average_score(self):
        return sum(self.grades) / len(self.grades)

#
# student_one = StudentInfo("Colum", "O'Siochru", [80, 68, 94, 92])
# print(student_one.grades)
# print(student_one.display_average_score)
# print(student_one.display_name)
# print(student_one.display_email)
