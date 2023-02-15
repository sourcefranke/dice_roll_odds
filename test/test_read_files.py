import unittest

from util.read_files import one_die


class MyTestCase(unittest.TestCase):
    def test_one_die(self):
        data = one_die()
        self.assertEqual(len(data.keys()), 6)
        for k in data:
            print(f"{k} : {data[k]}")


if __name__ == '__main__':
    unittest.main()
