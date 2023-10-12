import unittest
import io

from unittest.mock import mock_open, patch
from replacetext import api, open_file, dictionary, source_text, save_source_text, data_input

class TestAPI(unittest.TestCase):
    def test_api_success(self):
        with patch('requests.get') as m_requests_get:
            m_requests_get.return_value.json.return_value = {'key': 'value'}
            result = api('https://test_api.net')
            self.assertEqual(result, {'key': 'value'})


    def test_api_fail(self):
        with patch ('sys.stdout', new_callable=io.StringIO) as m_stdout:
            with patch('requests.get') as m_requests_get:
                m_requests_get.side_effect = ValueError  # вызов ValueError

                with self.assertRaises(SystemExit):
                    api('https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/data.json')
                        
                self.assertIn('Произошла ошибка, при указание ссылки!', m_stdout.getvalue().strip())


class TestOpenFile(unittest.TestCase):
    def test_open_file_sucess(self):
        with patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}'):
            result = open_file('test_open_file.json')
            self.assertEqual(result, {'key': 'value'})


    def test_open_file_fail(self):
        with patch('builtins.open', side_effect=FileNotFoundError):
            with self.assertRaises(SystemExit):
                open_file('test_open_file.json')


class TestDictionary(unittest.TestCase):
    def test_dictionary(self):
        with patch('builtins.open', new_callable=mock_open, read_data='[{"replacement": "LoVe", "source": "Love"}, {"replacement": "Car", "source": "None"}]'):
            result = dictionary('test_dictionary.json')
            self.assertDictEqual(result, {"LoVe": {"replacement": "LoVe", "source": "Love"}, "Car": {"replacement": "Car", "source": "None"}})
            

class TestSourceText(unittest.TestCase):
    def test_source_text(self):
        data = ['new task']
        with patch('builtins.open', new_callable=mock_open, read_data='[{"replacement": "new", "source": "old"}]') as f_path:
            result = source_text(data, f_path)
            self.assertEqual(result, ['old task'])


class TestSaveSourceText(unittest.TestCase):
    def test_save_source_text(self):
        with patch('replacetext.source_text', return_value=["Denis", "How are you?", "I hope the code is ok!"]) as check_source_text:
            data = 'test'
            f_path = 'replacement.json'

            save_source_text(data, f_path)
            check_source_text.assert_called_once_with(data, f_path)  # проверка что вызвана один раз


if __name__ == '__main__':
    unittest.main()