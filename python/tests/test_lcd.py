import pytest

from lcd.lcd import convert


class TestLcd:

    @pytest.mark.skip(reason="test currently disabled")  # Comment or remove this line to enable this test case
    def test_acceptance_test(self) -> None:
        value = 120120120
        expected = ''.join([
            "    _  _     _  _     _  _ \n",
            "  | _|| |  | _|| |  | _|| |\n",
            "  ||_ |_|  ||_ |_|  ||_ |_|\n",
        ])
        assert (expected == convert(value))
