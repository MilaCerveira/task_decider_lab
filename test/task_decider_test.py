import unittest
from src.task import Task
from src.task_decider import *


class TaskDecider(unittest.TestCase):
    def setUp(self):
        self.task1 = Task("wash dishes", 15)
        self.task2 = Task("cook dinner", 45)
        self.task3 = Task("clean windows", 30)

    def test_get_prefered_option(self):
        self.assertEqual(self.task1, get_preferred_option(
            self.task1, self.task2))
