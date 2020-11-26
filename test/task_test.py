import unittest
from src.task import Task


class TestTask(unittest.TestCase):
    def setUp(self):
        self.task1 = Task("wash dishes", 15)
        self.task2 = Task("cook dinner", 45)
        self.task3 = Task("clean windows", 30)

    def test_task_has_description(self):
        self.assertEqual("wash dishes", self.task1.description)

    def test_task_has_duration(self):
        self.assertEqual(15, self.task1.duration)
