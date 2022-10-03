import unittest

class TestAbs(unittest.TestCase): #Создать класс, который должен наследоваться от класса TestCase:class TestAbs(unittest.TestCase)
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()

#для запуска в консоли(терминале) пишем python test_abs_project.py
