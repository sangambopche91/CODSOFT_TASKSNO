import unittest
from main import AI, HUMAN, EMPTY, get_winner, is_draw, get_ai_move


class TestTicTacToe(unittest.TestCase):

    def test_row_winner(self):
        board = ["X", "X", "X", " ", "O", " ", " ", " ", " "]
        self.assertEqual(get_winner(board), HUMAN)

    def test_diagonal_winner(self):
        board = ["O", "X", "X", " ", "O", " ", "X", " ", "O"]
        self.assertEqual(get_winner(board), AI)

    def test_draw(self):
        board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        self.assertTrue(is_draw(board))

    def test_ai_winning_move(self):
        board = ["O", "O", " ", "X", "X", " ", " ", " ", " "]
        self.assertEqual(get_ai_move(board), 2)

    def test_ai_blocks_player(self):
        board = ["X", "X", " ", "O", " ", " ", " ", " ", "O"]
        self.assertEqual(get_ai_move(board), 2)

    def test_ai_chooses_empty_position(self):
        board = ["X", " ", " ", " ", "O", " ", " ", " ", " "]
        move = get_ai_move(board)
        self.assertIsNotNone(move)
        self.assertEqual(board[move], EMPTY)


if __name__ == "__main__":
    unittest.main()
