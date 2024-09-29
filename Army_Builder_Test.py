import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    team_name = Teams()
    print(team_name.add_team('Grogars'))


if __name__ == '__main__':
    unittest.main()
