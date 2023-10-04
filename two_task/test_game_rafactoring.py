import unittest
import io

from unittest.mock import patch
from game_refactoring import main 

class TestGame(unittest.TestCase):

    @patch('builtins.input', side_effect = ['да', '7']) # цифра 1-10, ждём пока не выводит 'OK' в терминале 
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_random_number (self, m_stdout, m_input):
        main()
        self.assertIn('Вы угадали число!', m_stdout.getvalue().strip())


if __name__ == '__main__':
    unittest.main()


