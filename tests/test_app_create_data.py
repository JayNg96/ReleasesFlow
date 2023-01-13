import unittest
import sys
sys.path.append('..')
from app import *


class TestCreateData(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_columns(self):
        student_data = Student_Data.__table__
        columns = student_data.columns.keys()
        self.assertEqual(columns, ['Student_ID', 'Name', 'Preference', 'Status'])

    def test_primary_key(self):
        student_data = Student_Data.__table__
        pk = student_data.primary_key.columns.keys()
        self.assertEqual(pk, ['Student_ID'])

    def test_repr_method(self):
        student = Student_Data(Student_ID='S12345678', Name='John Doe', Preference='Engineering', Status='Unassigned')
        self.assertEqual(str(student), "<Student ID: 'S12345678'>")
        student.Status = 'Pending confirmation'
        self.assertEqual(str(student), "<Student ID: 'S12345678'>")

    def setUp(self):
        self.student = Student_Data(Student_ID='12345678', Name='John Smith', Preference='Software Development',
                                    Status='Unassigned')

    def test_student_id(self):
        self.assertEqual(self.student.Student_ID, '12345678')

    def test_name(self):
        self.assertEqual(self.student.Name, 'John Smith')

    def test_preference(self):
        self.assertEqual(self.student.Preference, 'Software Development')

    def test_status(self):
        self.assertEqual(self.student.Status, 'Unassigned')


    def test_columns(self):
        company_data = Company_Data.__table__
        columns = company_data.columns.keys()
        self.assertEqual(columns, ['Company_Name', 'Job_Role', 'Company_Contact', 'Email'])


if __name__ == '__main__':
    unittest.main()