import unittest

from lcd.lcd import convert


class LcdTest(unittest.TestCase):

    @unittest.skip("test currently disabled")  # Comment or remove this line to enable this test case
    def test_acceptance_test(self):
        value = 120120120
        expected = [
            "    _  _     _  _     _  _ \n",
            "  | _|| |  | _|| |  | _|| |\n",
            "  ||_ |_|  ||_ |_|  ||_ |_|\n",
        ]
        self.assertEqual(''.join(expected), convert(value))


if __name__ == "__main__":
    unittest.main()
