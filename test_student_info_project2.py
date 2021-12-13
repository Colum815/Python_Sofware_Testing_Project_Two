"""
The main difference between project two (this file) and project_one is that I have included a setUp
and tearDown function. The setUp function allows me to set up the information to test in every function in the file.
This saves time by not having to write out the same information for each function.
The tearDown function would contain code to perform clean up operations after each test.
I will use the tearDown function in future projects. I have included print statements for the purpose of
displaying the order of execution.
"""
import unittest
from student_info_project_2 import StudentInfo


class TestingStudent(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.student1 = StudentInfo("Colum", "O'Siochru", [80, 70, 90, 98])
        self.student2 = StudentInfo("John", "O'Brien", [40, 56, 78, 67])

    def tearDown(self):
        print("tearDown")
        pass

    def test_display_name(self):
        print("test_display_name")
        self.assertEqual(self.student1.display_name, "Colum O'Siochru")
        self.assertEqual(self.student2.display_name, "John O'Brien")

    def test_display_email(self):
        print("test_display_email")
        self.assertEqual(self.student1.display_email, "columo'siochru@yahoo.ie")
        self.assertEqual(self.student2.display_email, "johno'brien@yahoo.ie")

    def test_display_average(self):
        print("test_display_average")
        self.assertEqual(self.student1.display_average_score, 84.5)
        self.assertEqual(self.student2.display_average_score, 60.25)
