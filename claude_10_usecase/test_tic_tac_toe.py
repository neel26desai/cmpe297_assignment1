import unittest
from tic_tac_toe import is_board_full, check_win, easy_ai_move, medium_ai_move, hard_ai_move

class TestTicTacToe(unittest.TestCase):
    def test_is_board_full(self):
        self.assertTrue(is_board_full(['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']))
        self.assertFalse(is_board_full(['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', ' ']))
        self.assertFalse(is_board_full([' ' for _ in range(9)]))

    def test_check_win(self):
        # Test rows
        self.assertTrue(check_win(['X', 'X', 'X', 'O', 'O', ' ', ' ', ' ', ' '], 'X'))
        self.assertTrue(check_win([' ', ' ', ' ', 'O', 'O', 'O', 'X', 'X', ' '], 'O'))
        
        # Test columns
        self.assertTrue(check_win(['X', 'O', ' ', 'X', 'O', ' ', 'X', ' ', ' '], 'X'))
        self.assertTrue(check_win(['O', 'X', ' ', 'O', 'X', ' ', 'O', ' ', ' '], 'O'))
        
        # Test diagonals
        self.assertTrue(check_win(['X', 'O', ' ', 'O', 'X', ' ', ' ', ' ', 'X'], 'X'))
        self.assertTrue(check_win([' ', 'O', 'X', ' ', 'X', 'O', 'X', ' ', ' '], 'X'))
        
        # Test no win
        self.assertFalse(check_win(['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', ' '], 'X'))
        self.assertFalse(check_win(['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', ' '], 'O'))

    def test_easy_ai_move(self):
        board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', ' ']
        move = easy_ai_move(board)
        self.assertEqual(move, 8)  # Only empty space

        board = [' ' for _ in range(9)]
        move = easy_ai_move(board)
        self.assertTrue(0 <= move < 9)  # Random move within board

    def test_medium_ai_move(self):
        # Test winning move
        board = ['O', 'O', ' ', 'X', 'X', ' ', ' ', ' ', ' ']
        self.assertEqual(medium_ai_move(board), 2)

        # Test blocking move
        board = ['X', 'X', ' ', 'O', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(medium_ai_move(board), 2)

        # Test random move when no winning or blocking move
        board = ['X', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ']
        move = medium_ai_move(board)
        self.assertNotEqual(move, 4)  # Should not choose the occupied center
        self.assertTrue(0 <= move < 9)

    def test_hard_ai_move(self):
        # Test winning move
        board = ['O', 'O', ' ', 'X', 'X', ' ', ' ', ' ', ' ']
        self.assertEqual(hard_ai_move(board), 2)

        # Test blocking move
        board = ['X', 'X', ' ', 'O', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(hard_ai_move(board), 2)

        # Test strategic move
        board = ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        move = hard_ai_move(board)
        self.assertTrue(move in [4, 0, 2, 6, 8])  # Center or corners are best moves

if __name__ == '__main__':
    unittest.main()