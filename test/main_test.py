from main import get_weather
import unittest
from unittest.mock import patch

class Test(unittest.TestCase):
    @patch('main.requests.get')
    def test_get_weather():
        mock_get.return_value.json.return_value = {"temperature": 22}
        result = get_weather()
        self.assertTrue (result, 22)

if __name__ == '__main__':
    unittest.main()