from django.test import TestCase

from app.calc import add 

class CalcTests(TestCase): 

    def test_one(self):
        self.assertEqual(add(2,2),4)