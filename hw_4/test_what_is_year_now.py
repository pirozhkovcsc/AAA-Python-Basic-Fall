import unittest
from unittest.mock import patch
import json
from what_is_year_now import what_is_year_now


class TestWhatIsYearNow(unittest.TestCase):
    """Проводит тесты для функции what_is_year_now"""

    @patch("what_is_year_now.urllib.request.urlopen")
    def test_year_format_ymd(self, mock_urlopen):
        # Для формата YYYY-MM-DD
        mock_response = {"currentDateTime": "2023-01-01"}
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            json.dumps(mock_response)

        expected_year = 2023
        self.assertEqual(
            what_is_year_now(),
            expected_year,
            "Должен вернуть год из формата YYYY-MM-DD",
        )

    @patch("what_is_year_now.urllib.request.urlopen")
    def test_year_format_dmy(self, mock_urlopen):
        # Для формата DD.MM.YYYY
        mock_response = {"currentDateTime": "01.02.2020"}
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            json.dumps(mock_response)

        expected_year = 2020
        self.assertEqual(
            what_is_year_now(),
            expected_year,
            "Должен вернуть год из формата DD.MM.YYYY",
        )

    @patch("what_is_year_now.urllib.request.urlopen")
    def test_invalid_date_format(self, mock_urlopen):
        # Для неверного формата
        mock_response = {"currentDateTime": "2020/05/06"}
        mock_urlopen.return_value.__enter__.return_value.read.return_value = \
            json.dumps(mock_response)

        with self.assertRaises(ValueError):
            what_is_year_now()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
