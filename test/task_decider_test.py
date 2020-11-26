import unittest
from src.task import Task
from src.task_decider import *


class TaskDecider(unittest.TestCase):
    def setUp(self):
        self.task1 = Task("wash dishes", 15)
        self.task2 = Task("cook dinner", 45)
        self.task3 = Task("clean windows", 30)

    def test_get_prefered_option(self):
        self.assertEqual(self.task1.description, get_preferred_option(
            self.task1, self.task2))


# clean window, wash dishes return clean windows
# wash dishes, cook dinner return wash dishes
# cook diner clean windows return cook dinner

    def test_get_prefered_option__wash_dishes(self):
        self.assertEqual("wash dishes", get_preferred_option(
            self.task1, self.task2))
