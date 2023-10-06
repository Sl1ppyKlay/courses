import unittest
import io
from unittest.mock import MagicMock, mock_open, patch
from replacetext import api, open_file

class TestSystemReplacement(unittest.TestCase):

    
    @patch('requests.get')  # иммитация requests
    def test_api_success(self, m_requests_get):  # проверка работы api удачно
        response = MagicMock()  # иммитация ответа http-запроса

        response.json.return_value = {'key': 'value'}
        m_requests_get.return_value = response

        result = api('https://blata.net')
        self.assertEqual(result, {'key': 'value'})


    @patch('requests.get')  # иммитация requests
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_api_fail(self, m_stdout, m_requests_get):  # проверка работы api неудачно
        m_requests_get.side_effect = ValueError  # вызов ValueError

        with self.assertRaises(SystemExit):
            api('https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/data.json')
                
        self.assertIn('Произошла ошибка, при указание ссылки!', m_stdout.getvalue())


    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
    def test_open_file_sucess(self, m_file):  # проверка открытия файла удачно
        result = open_file('blata_net.json')
        self.assertEqual(result, {'key': 'value'})


    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_open_file_fail(self, m_file):  # проверка открытия файла неудачно 
        with self.assertRaises(SystemExit):
            open_file('blata_net.json')
        

if __name__ == '__main__':
    unittest.main()