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


# wash dishes, wash clothes return wash dishes
# cook dinner, do ironing return cook dinner
# clean windows, do ironing return clean windows
# do ironing, wash dishes return do ironing
#

    def test_get_prefered_option__wash_dishes(self):
        self.assertEqual("wash dishes", get_preferred_option(
            self.task1, self.task2))

    def test_get_prefered_option__clean_windows(self):
        self.assertEqual("clean windows", get_preferred_option(
            self.task3, self.task1))

    def test_get_prefered_option__cook_dinner(self):
        self.assertEqual("cook dinner", get_preferred_option(
            self.task2, self.task3))
